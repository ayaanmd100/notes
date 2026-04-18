import os, re

known_cmds = {
    'begin','end','frac','overbrace','sqrt','tfrac','underbrace',
    'Pr','arccos','arcsin','arctan','arg','cos','cosh','cot','coth','csc',
    'deg','det','dim','exp','gcd','hom','inf','ker','lg','lim','ln','log',
    'max','min','sec','sin','sinh','sup','tan','tanh',
    'bar','ddot','dot','hat','overline','tilde','underline','vec',
    'iiiint','iiint','iint','oiiint','oiint','oint',
    'left','right',
    'Delta','Gamma','Lambda','Omega','Phi','Pi','Psi','Sigma','Theta','Xi',
    'alpha','angle','approx','ast','beta','cap','cdot','chi','circ','cong','cup',
    'degree','delta','div','ell','emptyset','epsilon','equiv','eta',
    'exists','forall','gamma','ge','geq','gets','hbar','in','infty','int',
    'iota','kappa','lambda','langle','lbrace','lceil','le','leftarrow',
    'leq','lfloor','mp','mu','nabla','ne','neq','notin','nu','omega',
    'omicron','oplus','parallel','partial','perp','phi','pi','pm','prime',
    'prod','propto','psi','rangle','rbrace','rceil','rfloor','rho',
    'rightarrow','sigma','sim','subset','subseteq','sum','tau','therefore',
    'theta','times','to','upsilon','xi','zeta',
    'binom','quad','qquad',
    'text',  # keep text to see if any remain
}

notes_dir = os.path.join(os.path.dirname(__file__), 'notes')
cmd_re = re.compile(r'\\([a-zA-Z]+)')

for fname in sorted(os.listdir(notes_dir)):
    if not fname.endswith('.tex'):
        continue
    text = open(os.path.join(notes_dir, fname), encoding='utf-8').read()
    for m in cmd_re.finditer(text):
        cmd = m.group(1)
        if cmd not in known_cmds:
            pos = m.start()
            ctx = text[max(0, pos-15):pos+25]
            print(f"{fname}: \\{cmd}  <- {repr(ctx)}")
