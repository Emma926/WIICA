IR_name = {
'1':'Ret',
'2':'Br',
'3':'Switch',
'4':'IndirectBr',
'5':'Invoke',
'6':'Resume',
'7':'Unreachable',
'8':'Add',
'9':'FAdd',
'10':'Sub',
'11':'FSub',
'12':'Mul',
'13':'FMul',
'14':'UDiv',
'15':'UDiv',
'16':'FDiv',
'17':'URem',
'18':'SRem',
'19':'FRem',
'20':'Shl',
'21':'LShr',
'22':'AShr',
'23':'And',
'24':'Or',
'25':'Xor',
'26':'Alloca',
'27':'Load',
'28':'Store',
'29':'GetElementPtr',
'30':'Fence',
'31':'AtomicCmpXchg',
'32':'AtomicRMW',
'33':'Trunc',
'34':'ZExt',
'35':'SExt',
'36':'FPToUI',
'37':'FPToSI',
'38':'UIToFP',
'39':'SIToFP',
'40':'FPTrunc',
'41':'FPExt',
'42':'PtrToInt',
'43':'IntToPtr',
'44':'BitCast',
'45':'AddrSpaceCast',
'46':'ICmp',
'47':'FCmp',
'48':'PHI',
'49':'Call',
'50':'Select',
'53':'VAArg',
'54':'ExtractElement',
'55':'InsertElement',
'56':'ShuffleVector',
'57':'ExtractValue',
'58':'InsertValue',
'59':'LandingPad',
}

IR_MOVE = ['Trunc' , 'ZExt' , 'SExt' , 'FPToUI' , 'FPToSI' , 'UIToFP' , 'SIToFP' , 'FPTrunc' , 'FPExt' , 'PtrToInt' , 'IntToPtr' , 'BitCast' , 'AddrSpaceCast' , 'ExtractElement' , 'InsertElement' , 'ShuffleVect,' , 'ExtractValue' , 'InsertValue']

IR_UNCOND_BRANCH = ['Ret' , 'IndirectBr' , 'Invoke' , 'Resume' , 'Call']
IR_COND_BRANCH = ['Br', 'Switch', 'Select']
IR_BRANCH = [item for pair in zip(IR_UNCOND_BRANCH, IR_COND_BRANCH) for item in pair]
IR_COMPUTE = ['Add' , 'FAdd' , 'Sub' , 'FSub' , 'Mul' , 'FMul' , 'UDiv' , 'SDiv' , 'FDiv' , 'URem' , 'SRem' , 'FRem' , 'Shl' , 'LShr' , 'AShr' , 'And' , 'Or' , 'Xor' , 'ICmp' , 'FCmp']
IR_MEMORY = ['Load', 'Store', 'AtomitCmpXchg', 'AtomicRMW']

#IR_MOVE_ID = [1,17,18,23]
#IR_UNCOND_BRANCH_ID = [20,27,28,29,30,41,40,32,33,34,39,43,44,52,54,65,68,69,31]
#IR_COND_BRANCH_ID = [21 , 22]
