# 导入
import argparse
import traceback

# 全局变量
# 入参解析
parser = argparse.ArgumentParser(description='nand2tetris course assembler')
parser.add_argument('filenames', type=str, nargs='+', help='asm files that want to translate into hack machine language.')
args = parser.parse_args()

# 内置Symbol table
INNER_SYMBOL_TABLE = {
    "R0": "0",
    "R1": "1",
    "R2": "2",
    "R3": "3",
    "R4": "4",
    "R5": "5",
    "R6": "6",
    "R7": "7",
    "R8": "8",
    "R9": "9",
    "R10": "10",
    "R11": "11",
    "R12": "12",
    "R13": "13",
    "R14": "14",
    "R15": "15",
    "SCREEN": "16384",
    "KBD": "24576",
    "SP": "0",
    "LCL": "1",
    "ARG": "2",
    "THIS": "3",
    "THAT": "4"
}

COMP_TABLE = {
    "0":   "0101010",
    "1":   "0111111",
    "-1":  "0111010",
    "D":   "0001100",
    "A":   "0110000",
    "M":   "1110000",
    "!D":  "0001101",
    "!A":  "0110001",
    "!M":  "1110001",
    "-D":  "0001111",
    "-A":  "0110011",
    "-M":  "1110011",
    "D+1": "0011111",
    "A+1": "0110111",
    "M+1": "1110111",
    "D-1": "0001110",
    "A-1": "0110010",
    "M-1": "1110010",
    "D+A": "0000010",
    "D+M": "1000010",
    "D-A": "0010011",
    "D-M": "1010011",
    "A-D": "0000111",
    "M-D": "1000111",
    "D&A": "0000000",
    "D&M": "1000000",
    "D|A": "0010101",
    "D|M": "1010101"
}

DEST_TABLE = {
    "":    "000",
    "M":   "001",
    "D":   "010",
    "MD":  "011",
    "A":   "100",
    "AM":  "101",
    "AD":  "110",
    "AMD": "111"
}

JUMP_TABLE = {
    "":    "000",
    "JGT": "001",
    "JEQ": "010",
    "JGE": "011",
    "JLT": "100",
    "JNE": "101",
    "JLE": "110",
    "JMP": "111"
}

# 类
# 异常类
class TranslateError(Exception):
    def __init__(self, description="Invalid asm file input"):
        self.description = description
        self.laststack = traceback.extract_stack()[0]

    def __str__(self):
        return f"TranslateError: {self.description} ---- at line: {self.laststack.lineno} in \"{self.laststack.filename}\"" + \
               f"\n    {self.laststack.line}"

# 函数
def readfile(filename):
    # 读入指令, 去除空格、注释
    instructions = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            instruction = line[:line.find("//")]
            instruction = instruction.replace(" ", "")
            if instruction:
                instructions.append(instruction)
    return instructions


def asm_to_machine(instructions):
    # Symbol table模版
    symbol_table = INNER_SYMBOL_TABLE.copy()
    # 添加所有LABEL
    add_label(instructions, symbol_table)

    # Symbol替换
    instructions = substitute_symbol(instructions, symbol_table)

    # 翻译每一条指令
    machine_codes = []
    for instruction in instructions:
        machine_codes.append(translate_instruction(instruction))

    return machine_codes
    
def add_label(instructions, symbol_table):
    count = 0
    for instruction in instructions:
        if instruction[0] == "(" and instruction[-1] == ")":
            symbol = instruction[1:-1]
            if symbol not in symbol_table:
                symbol_table[symbol] = count
            else:
                raise TranslateError(f"Redefine same LABEL ({symbol})")
        else:
            count += 1

def substitute_symbol(instructions, symbol_table):
    address = 16
    new_instructions = []

    for instruction in instructions:
        # 处理LABEL, pass
        if instruction[0] == "(" and instruction[-1] == ")":
            continue

        # @开头的指令如果不是立即数则尝试替换
        if instruction[0] == "@":
            symbol = instruction[1:]
            if not symbol.isdigit():
                if symbol not in symbol_table:
                    symbol_table[symbol] = address
                    address += 1
                instruction = f"@{symbol_table[symbol]}"
        new_instructions.append(instruction)
    return new_instructions

def translate_instruction(instruction):
    # A类指令
    if instruction[0] == "@":
        num = int(instruction[1:])
        if num >= 32768:
            raise TranslateError(f"Immediate number {num} >= 32768")
        else:
            b_num = bin(num)[2:]
            return "0" + "0" * (15 - len(b_num)) + b_num

    # C类指令
    # dest = comp ; jump
    equal = instruction.find("=")
    semicolon = instruction.find(";")
    dest, jump = "", ""
    if equal != -1:
        dest = instruction[:equal]
    if semicolon != -1:
        jump = instruction[semicolon+1:]
    comp = instruction.replace(f"{dest}=", "").replace(f";{jump}", "")

    try:
        machine_code = "111" + COMP_TABLE[comp] + DEST_TABLE[dest] + JUMP_TABLE[jump]
    except IndexError:
        raise TranslateError("Invalid instruction")

    return machine_code

def write_to_file(machine_codes, filename):
    filename = filename.replace(".asm", ".hack")
    s = "\n".join(machine_codes)
    with open(filename, "w") as f:
        f.write(s)

# main
if __name__ == '__main__':
    filename = args.filenames[0]
    instructions = readfile(filename)
    machine_codes = asm_to_machine(instructions)
    write_to_file(machine_codes, filename)




