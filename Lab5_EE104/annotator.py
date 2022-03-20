#   Copyright (c) 2017, Xilinx, Inc.
#   All rights reserved.
#
#   Redistribution and use in source and binary forms, with or without
#   modification, are permitted provided that the following conditions are met:
#
#   1.  Redistributions of source code must retain the above copyright notice,
#       this list of conditions and the following disclaimer.
#
#   2.  Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#
#   3.  Neither the name of the copyright holder nor the names of its
#       contributors may be used to endorse or promote products derived from
#       this software without specific prior written permission.
#
#   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
#   AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
#   THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
#   PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
#   CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
#   EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
#   PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
#   OR BUSINESS INTERRUPTION). HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
#   WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
#   OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
#   ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import re
import itertools
from copy import deepcopy


__author__ = "Naveen Purushotham"
__copyright__ = "Copyright 2017, Xilinx"
__email__ = "pynq_support@xilinx.com"


def wave_to_bitstring(wave):
    """Function to convert a pattern consisting of `l`, `h`, and dot to a
    sequence of `0` and `1`.

    Parameters
    ----------
    wave : str
        The input string to convert.

    Returns
    -------
    str
        A bit sequence of 0's and 1's.

    """
    substitution_map = {'l': '0', 'h': '1'}

    def delete_dots(match):
        return substitution_map[match.group()[0]] * len(match.group())

    wave_regex = re.compile(r'[l]\.*|[h]\.*')
    return re.sub(wave_regex, delete_dots, wave)


class Annotator:
    """Class for the WaveDrom Annotator.

    This class can update the WaveDrom dictionary with additional annotations.
    Users can group signals as buses or add custom annotations.

    Attributes
    ----------
    multibit_bus_colors : dict
        A dictionary to store the color codes for the allowed wavelanes.
    direction_values : tuple
        The list of allowed strings that specify direction of a signal bus. 
    radix_values : tuple
        The list of allowed strings that specify radix of a signal bus.
    group_by_values : tuple
        The list of allowed strings that specify how signals are to be grouped.

    """

    def __init__(self, raw_wavejson):
        """Return a new WaveDrom annotator object.

        Parameters
        ----------
        raw_wavejson : dict
            A dictionary storing the patterns in WaveJSON format.

        """
        self._wavejson = deepcopy(raw_wavejson)
        self.multibit_bus_colors = dict(blue='5', orange='4', yellow='3',
                                        white='2')
        self.direction_values = ('reverse', 'same')
        self.radix_values = ('decimal', 'binary')
        self.group_by_values = ('transition', 'cycle')

    def group_signals(self, signal_names=None, samples=None, radix='decimal',
                      direction='same', color='yellow', label_map=None,
                      group_by='transition'):
        """Group a list of signals as a vector bus

         This method will take a signal list and generate an equivalent
         vector bus. The signal list will contain the names of the signals 
         as specified in the input waveJSON dict. Users can then update the 
         waveJSON dict with the generated output vector bus parameters 

         Parameters
         ----------
         signal_names : list
            A list of signal names, names are the same as the input dict
            specification. Element 0 is MSB and element -1 is LSB
         samples : int
             The number of smaples to be grouped not exceeding total samples
         radix: str
             String that defines which radix is displayed in the vector bus
         direction : str
             String that defines direction of the vector bus 
         label_map : dict
             Vector value can be mapped to specific label using this dict
         group_by: str
            Vector are created based on per-clock or per-transition basis

         Returns
         -------
         str, list
             str - Actual wave string of the vector bus.
             list - list contains the values of the vector bus

         """

        def map_labels(current_labels):
            """Updates the vector values to labels specified using label_map
            
            """

            def label_lookup(label):
                if label_map is not None:
                    return label_map[label] if label in label_map.keys() \
                        else label
                else:
                    return label

            for index, v in enumerate(current_labels):
                current_labels[index] = label_lookup(v)

        def predicate(signal):
            """Filters the signal names of the bus from the full waveJSON dict
            
            """
            try:
                return signal['name'] in signal_names
            except:
                return False

        # Check validity of inputs: radix, drection and group_by
        if radix not in self.radix_values:
            raise ValueError(
                "Possible values for radix are {}".format(self.radix_values))
        if direction not in self.direction_values:
            raise ValueError(
                "Possible values for direction are {}".format(
                    self.direction_values))
        if group_by not in self.group_by_values:
            raise ValueError(
                "Possible values for group_by are {}".format(
                    self.group_by_values))

        # Reverse signal order to change vector bus direction
        signal_names.reverse() if direction == 'reverse' else None

        # Lists to store waves and labels of the signals that are grouped
        waves, labels_per_cycle = [], []

        # Filter and sort the signals using a generator pipeline
        signals = itertools.chain.from_iterable(self._wavejson['signal'])
        filtered_signals = filter(predicate, signals)
        sorted_signals = sorted(filtered_signals,
                                key=lambda x: signal_names.index(x['name']))

        # Convert the wavestrings of the sorted signals to bitstrings
        waves = [wave_to_bitstring(s['wave']) for s in sorted_signals]

        # Get length of the total samples
        total_samples = 0
        if waves:
            total_samples = len(waves[0])

        # Samples currently processed for annotation
        if not samples or samples > total_samples:
            samples = total_samples

        # Create vector bus from individual wavestrings
        for j in range(samples):
            bits_per_cycle = [waves[i][j] for i in range(len(signal_names))]
            labels_per_cycle.extend([''.join(bits_per_cycle)])

        # Set radix of the signal bus
        if radix == 'decimal':
            labels_per_cycle = list(map(lambda x: str(int(x, 2)),
                                        labels_per_cycle))
        else:
            pass

        # Label vectors if a label_map is specified
        map_labels(labels_per_cycle)

        # Make wave string with the specified color
        bus_wave_cstring = self.multibit_bus_colors[color] * samples

        # Converge consecutive identical vectors to single transition
        # Create labels and count how many consecutive identical vectors occured
        labels_per_transition, count_unique = [], []
        for u, c in itertools.groupby(labels_per_cycle):
            labels_per_transition.append(u)
            count_unique.append(len(list(c)))

        # Create wavestring on per-transition basis
        bus_wave_tstring = ""
        for i, j in enumerate(count_unique):
            bus_wave_tstring += (
                self.multibit_bus_colors[color] + "." * (j - 1))

        # Return string and list based on group_by
        # These will be used by update_wavedict method
        if group_by == 'transition':
            return bus_wave_tstring, labels_per_transition
        else:
            return bus_wave_cstring, labels_per_cycle

    # Insert gap in dict while updating with annotation
    def _insert_gap(self):
        """Inserts a gap in waveform for clarity

        This method is called internally while updating the output dict.

        """
        self._wavejson['signal'].append({})

    # Update wavedict either with custom wave, grouped wave or annotation.
    def update_wavedict(self, sig_name, sig_wave, sig_data, gap=True):
        """Update the dict with new wave, vector bus or annotation
        
        Parameters
        ----------
        sig_name: str
            Name of the new wave, vector bus or annotation
        sig_wave: str
            string specification of the wave, vector bus
        sig_data: list
            List values or labels for each vector or annotation
        gap: bool
            Choose to insert gap or not    
        
        Returns
        -------
        dict
            updated dict which is either further updated with other items or 
            displayed using WaveDROM

        """
        if gap:
            self._insert_gap()
        elif not gap:
            pass
        else:
            raise ValueError("Possible values for gap are (True, False)")
        self._wavejson['signal'].append({"name": sig_name,
                                         "wave": sig_wave,
                                         "data": sig_data})
        return self._wavejson
