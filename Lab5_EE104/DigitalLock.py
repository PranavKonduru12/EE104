#Digital Lock Pick using FSM and Pattern Generators
'''
In this notebook we will use the FSM Generator to emulate a digital lock, and the Pattern Generator to enumerate a few possible 3-bit sequences. When the Pattern Generator presents the correct pattern the FSM Generator will reach the open state.
Original author: Naveen Puroshotham. The code was written for ZYNQ UltraSCALE board
Ported to ZYNQ-Z2: Christopher Pham
'''

#Step 1: Download the logictools overlay
from pynq.overlays.logictools import LogicToolsOverlay
from pynq.lib.logictools import Waveform

logictools_overlay = LogicToolsOverlay('logictools.bit')

#Step 2: Instantiate the Logiclools Controller
'''
Since we are running the Pattern Generator and the FSM Generator simultaneously we must use the Logictools Controller. The Logictools controller is part of the logictools overlay initialized at download time.
'''
logictools_controller = logictools_overlay.logictools_controller

#Step 3: Creating a Digital Lock using the FSM Generator
'''
In this step we write a specification for an FSM Generator that emulates a 3-digit lock. The bit at index 0 is the reset bit. The bit at index 1 is the New Code bit and will cause a state transition. Bits 2 through 5 are the pattern bits. Our lock will open when the 3-digit input sequence is 1 - 0 - 6.

We create five states: S0, S1, S2, Open, and Closed.

S0: The lock starts in the S0 state and transtions to S1 if it receives a 1 AND the New Code bit is asseted, or stays in S0 if reset is asserted. All other inputs transition to the Closed state.

S1: In the S1 state, the lock transitions to S2 if it receives an 0 AND the New Code bit is asserted or returns to S0 if reset is asserted. All other inputs transition to the Closed state.

S2: In the S2 state, the lock transitions to the Open state if it receieves a 6 as input AND the New Code bit is asserted, and returns to S0 if reset is asserted. All other inputs transition to the Closed state.

Open: The lock will remain in the Open state until the reset bit is asserted.

Closed: The lock will remain in the Closed state until the reset bit is asserted

The following cell implements our lock:
'''

'''
        For Arduino header, 
        pin numbers 0-13 correspond to D0-D13;
        pin numbers 14-19 correspond to A0-A5;
        pin numbers 20-21 correspond to SDA and SCL.
'''

fsm_spec = {
    'inputs': [('reset', 'D0'), ('new_code_digit', 'D1'), 
               ('digit_bit2', 'D2'),
               ('digit_bit1', 'D3'), 
               ('digit_bit0', 'D4')],
    'outputs': [('lock_status', 'D5')],
    'states': ['S0', 'S1', 'S2', 'open', 'closed'],
    'transitions': [['1----', 'S0', 'S0', '0'],
                    ['1----', 'S1', 'S0', '0'],
                    ['1----', 'S2', 'S0', '0'],
                    ['1----', 'closed', 'S0', '0'],

                    ['00---', 'S0', 'S0', '0'],
                    ['01001', 'S0', 'S1', '0'],
                    ['01000', 'S0', 'closed', '0'],
                    ['01010', 'S0', 'closed', '0'],
                    ['01011', 'S0', 'closed', '0'],
                    ['01100', 'S0', 'closed', '0'],
                    ['01101', 'S0', 'closed', '0'],
                    ['01110', 'S0', 'closed', '0'],
                    ['01111', 'S0', 'closed', '0'],

                    ['00---', 'S1', 'S1', '0'],
                    ['01000', 'S1', 'S2', '0'],
                    ['01001', 'S1', 'closed', '0'],
                    ['01010', 'S1', 'closed', '0'],
                    ['01011', 'S1', 'closed', '0'],
                    ['01100', 'S1', 'closed', '0'],
                    ['01101', 'S1', 'closed', '0'],
                    ['01110', 'S1', 'closed', '0'],
                    ['01111', 'S1', 'closed', '0'],

                    ['00---', 'S2', 'S2', '0'],
                    ['01000', 'S2', 'closed', '0'],
                    ['01001', 'S2', 'closed', '0'],
                    ['01010', 'S2', 'closed', '0'],
                    ['01011', 'S2', 'closed', '0'],
                    ['01100', 'S2', 'closed', '0'],
                    ['01101', 'S2', 'closed', '0'],
                    ['01110', 'S2', 'open', '0'],
                    ['01111', 'S2', 'closed', '0'],

                    ['0----', 'closed', 'closed', '0'],

                    ['1----', 'open', 'S0', '1'],
                    ['0----', 'open', 'open', '1']]}
					
					
pattern_generator.setup(up_counter,
                        stimulus_group_name='stimulus',
                        analysis_group_name='analysis')
                        
                        

#To observe our lock, we also need to set up the trace analyzer. We do this in the following cell:
print(logictools_controller.status)

#We can also observe the input and output pins that have been assigned to the inputs and outputs of the FSM Generator:
fsm_generator.input_pins
fsm_generator.output_pins

#Finally, we can observe the State Diagram for our Digital Lock.
fsm_generator.show_state_diagram()


#Step 4: Creating a "Lock Pick" using the Pattern Generator¶
'''
Now that we've created a lock (and conveniently forgotten the combination) we need to crack it. To do this, we will use the FSM Generator.

In the cell below, we specify what patterns the Pattern Generator will iterate through.
'''

reset =          'hl......' + 'hl......' + 'hl......' + 'hl......' + \
    'hl........' + 'hl......' + 'hl......'
new_code_digit = 'l.hlhlhl' + '..hlhlhl' + '..hlhlhl' + '..hlhlhl' + \
    '..hlhlhl..' + '..hlhlhl' + '..hlhlhl'

# digits:   _____1_2_6________0_1_6________1_1_6________2_0_6___
#    __1_0_6__________0_1_6________1_1_6___
digit_bit_2 = 'l.....hl' + '......hl' + '......hl' + '......hl' + \
    '......hl..' + '......hl' + '......hl'
digit_bit_1 = 'l...h..l' + '......hl' + '......hl' + '..hl..hl' + \
    '......hl..' + '......hl' + '......hl'
digit_bit_0 = 'l.hl....' + '....hl..' + '..h...l.' + '........' + \
    '..hl......' + '....hl..' + '..h...l.'


'''
        For Arduino header, 
        pin numbers 0-13 correspond to D0-D13;
        pin numbers 14-19 correspond to A0-A5;
        pin numbers 20-21 correspond to SDA and SCL.
'''
key_gen = {'signal': [
    ['stimulus',
     {'name': 'reset', 'pin': 'D19',
      'wave': reset},
     {'name': 'new', 'pin': 'D18',
      'wave': new_code_digit},
     {'name': 'Value_2', 'pin': 'D17',
      'wave': digit_bit_2},
     {'name': 'Value_1', 'pin': 'D16',
      'wave': digit_bit_1},
     {'name': 'Value_0', 'pin': 'D15',
      'wave': digit_bit_0}]],
    'foot': {'tock': 1, 'text': 'Key Generation'},
    'head': {'tick': 1, 'text': 'Key Generation'}}

waveform = Waveform(key_gen)
waveform.display()


#Now that we've created our Lock Pick, we need to generate output to apply it to our lock. First we set-up the pattern generator:
pattern_generator = logictools_overlay.pattern_generator
pattern_generator.trace(num_analyzer_samples=58)
pattern_generator.setup(key_gen,
                        stimulus_group_name='stimulus',
                        analysis_group_name='analysis', frequency_mhz=1)
                        

#Next, we observe the assigned outputs of the Pattern Generator:
pattern_generator.stimulus_pins


#Step 5: Breaking In:¶
'''
Now that we've created the two halves, we will run them together to break in. First we check the status of the Generators:
'''

print(logictools_controller.status)

#Next, apply the following loopback wiring to the Arduino header on the PYNQ-Z2 Board:
'''
D0-A5 (reset)
D1-A4 (new)
D2-A3 (bit 0)
D3-A2 (bit 1)
D4-A1 (bit 2)
'''


#Finally, Run the Lock and Lock Pick:
logictools_controller.run([pattern_generator, fsm_generator])
print(logictools_controller.status)


#Step 6: Display Waveforms
'''
When the Lock Pick has cracked the Lock we can observe the results. We do this using waveforms captured from the Trace Analyzer.
'''
pattern_generator.show_waveform()
fsm_generator.show_waveform()


#Step 7: Annotate and display waveforms¶
'''
However, the waveforms above have not been annotated, and it can be difficult to tell what is going on. In the following step we will annotate the waveforms shown above,

First, we create a dictionary mapping the state digits to state names:
'''

import copy

state_map_dict = {"0" : "S0",
                  "1" : "S1",
                  "2" : "S2",
                  "3" : "Open",
                  "4" : "Closed"}

annotated_wave = copy.deepcopy(fsm_generator.waveform.waveform_dict)

from annotator import Annotator

annotate = Annotator(annotated_wave)

state_sig_list = ['state_bit2', 'state_bit1', 'state_bit0']
state_wave, state_wave_data = annotate.group_signals(
    state_sig_list, samples=58, label_map=state_map_dict)

code_wave = "x.5....x..5....x..5....x..5....x..5......x..5....x..5....x"
code_data = ["1 2 6", "0 1 6", "1 1 6", "2 0 6", "1 0 6", "0 1 6", "1 1 6"]

lock_wave = "2.4....2..4....2..4....2..4....2..3......2..4....2..4....2"
lock_data = ["reset", "Error", "reset", "Error",
             "reset", "Error", "reset", "Error",
             "reset", "Success", "reset", "Error",
             "reset", "Error"]


annotate.update_wavedict("FSM State", state_wave, state_wave_data)
annotate.update_wavedict("code_value", code_wave, code_data)
final_annotated_wave = annotate.update_wavedict("Lock Status", lock_wave,
                                                lock_data)

final_annotated_wave['signal'][0][6]['node'] = \
    "........................................a................."
final_annotated_wave['signal'][6]['node'] = \
    ".......................................b.................."
final_annotated_wave['edge'] = ['b~>a unlocked']


#Finally, display the annotated waveform:
from pynq.lib.logictools.waveform import draw_wavedrom

draw_wavedrom(final_annotated_wave)



#Step 8: Reset the generators
logictools_controller.reset([pattern_generator, fsm_generator])
print(logictools_controller.status)


