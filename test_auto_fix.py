from agents.auto_fix_agent import auto_fix

fixed = auto_fix(
    "generated_code"
)

print(
    "Fixed Files:"
)

for f in fixed:

    print(f)