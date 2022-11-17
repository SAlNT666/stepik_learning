import re


reg_ex = r'(?:\b[AEIOUYaeiouy]|\b)(?:[BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz][AEIOUYaeiouy])*(?:[BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz]\b|\b)'
print(*[i for i in re.findall(reg_ex, input()) if i])
