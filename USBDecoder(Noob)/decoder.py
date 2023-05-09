#!/usr/bin/env python3

import sys
import os

mapping_shift = {
  0x02: '<Shift>',
  0x20: '<RShift>'
}

mapping = {
  0x00: ["", ""],
  0x01: ["ErrorRollOver", "ErrorRollOver"],
  0x02: ["POSTFail9", "POSTFail9"],
  0x03: ["ErrorUndefined", "ErrorUndefined"],
  0x04: ["a", "A"],
  0x05: ["b", "B"],
  0x06: ["c", "C"],
  0x07: ["d", "D"],
  0x08: ["e", "E"],
  0x09: ["f", "F"],
  0x0A: ["g", "G"],
  0x0B: ["h", "H"],
  0x0C: ["i", "I"],
  0x0D: ["j", "J"],
  0x0E: ["k", "K"],
  0x0F: ["l", "L"],
  0x10: ["m", "M"],
  0x11: ["n", "N"],
  0x12: ["o", "O"],
  0x13: ["p", "P"],
  0x14: ["q", "Q"],
  0x15: ["r", "R"],
  0x16: ["s", "S"],
  0x17: ["t", "T"],
  0x18: ["u", "U"],
  0x19: ["v", "V"],
  0x1A: ["w", "W"],
  0x1B: ["x", "X"],
  0x1C: ["y", "Y"],
  0x1D: ["z", "Z"],
  0x1E: ["1", "!"],
  0x1F: ["2", "@"],
  0x20: ["3", "#"],
  0x21: ["4", "$"],
  0x22: ["5", "%"],
  0x23: ["6", "^"],
  0x24: ["7", "&"],
  0x25: ["8", "*"],
  0x26: ["9", "("],
  0x27: ["0", ")"],
  0x28: ["Return", "Return"],
  0x29: ["ESCAPE", "ESCAPE"],
  0x2A: ["<BACKSPACE>", "<BACKSPACE>"],
  0x2B: ["Tab", "Tab"],
  0x2C: [" ", " "],
  # 0x2C: "Spacebar",
  0x2D: ["-", "_"],
  0x2E: ["=", "+"],
  0x2F: ["[", "{"],
  0x30: ["]", "}"],
  0x31: ["\\", "|"],
  0x32: ["Non-US"],
  0x33: [";", ":"],
  0x34: ["‘", "\""],
  0x35: ["Grave"],
  0x36: [",", "<"],
  0x37: [".", ">"],
  0x38: ["/", "?"],
  0x39: ["Capslock", "Capslock"],
  0x3A: ["F1", "F1"],
  0x3B: ["F2", "F2"],
  0x3C: ["F3", "F3"],
  0x3D: ["F4", "F4"],
  0x3E: ["F5", "F5"],
  0x3F: ["F6", "F6"],
  0x40: ["F7", "F7"],
  0x41: ["F8", "F8"],
  0x42: ["F9", "F9"],
  0x43: ["F10", "F10"],
  0x44: ["F11", "F11"],
  0x45: ["F12", "F12"],
  0x46: ["PrintScreen", "PrintScreen"],
  0x47: ["ScrollLock", "ScrollLock"],
  0x48: ["Pause", "Pause"],
  0x49: ["Insert", "Insert"],
  0x4A: ["Home", "Home"],
  0x4B: ["PageUp", "PageUp"],
  0x4C: ["DeleleForward", "DeleteForward"],
  0x4D: ["End", "End"],
  0x4E: ["PageDown", "PageDown"],
  0x4F: ["RightArrow", "RightArrow"],
  0x50: ["LeftArrow", "LeftArrow"]
  # [OMITTED REST OF CODES FOR BREVITY]
}
infile = sys.argv[1]
datasave = 'usbdataextracted'

os.system(r"tshark -nr %s -Y 'len(usbhid.data) == 8' -T fields -e usbhid.data > %s" % (infile, datasave))

with open (datasave, 'r') as f:
  data = f.readlines()

result = ''

for line in data:
  interrupt_byte = int(line[6:8], 16)
  shift_byte = int(line[0:2], 16)
  shift_key = 0
  # Remove the interrupted event, when two keys are pressed at the same time.
  if interrupt_byte != 0x00:
    continue

  if shift_byte in mapping_shift:
    shift_key = 1

  normal_byte = int(line[4:6], 16)

  if normal_byte in mapping:
    stringed = mapping[normal_byte][shift_key]

  if stringed == mapping[0x2A][0]:
    # if backspace, remove one
    result = result[:-1]
  else:
    result += stringed
    
print(result)
