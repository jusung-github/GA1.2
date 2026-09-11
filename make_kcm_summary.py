from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
cases = [
    (1, 1, 1, 'Very large displacement; very fast and lively response', 'Strong'),
    (1, 1, 10, 'Very large displacement; low damping; longer period', 'Strong'),
    (1, 1, 100, 'Very large displacement; low damping; slow but strong motion', 'Strong'),
    (1, 10, 1, 'Large displacement; moderate damping; relatively fast', 'Moderate'),
    (1, 10, 10, 'Large displacement; moderate damping; noticeable oscillation', 'Moderate'),
    (1, 10, 100, 'Large displacement; slower response; moderate damping', 'Moderate'),
    (1, 100, 1, 'Large motion but strongly damped', 'Weak'),
    (1, 100, 10, 'Large motion; strong damping; reduced oscillation', 'Weak'),
    (1, 100, 100, 'Large displacement; strong damping; slow response', 'Weak'),
    (10, 1, 1, 'Moderate-to-large motion; very little damping', 'Strong'),
    (10, 1, 10, 'Moderate motion; low damping; visible oscillation', 'Strong'),
    (10, 1, 100, 'Moderate motion; slow period; low damping', 'Strong'),
    (10, 10, 1, 'Moderate motion; reasonable damping', 'Moderate'),
    (10, 10, 10, 'Baseline case: balanced response', 'Moderate'),
    (10, 10, 100, 'Moderate response; slower motion', 'Moderate'),
    (10, 100, 1, 'Small displacement; strongly damped', 'Very weak'),
    (10, 100, 10, 'Reduced response; damped motion', 'Very weak'),
    (10, 100, 100, 'Small displacement; damped and slow', 'Very weak'),
    (100, 1, 1, 'Small displacement; weak damping; fast but not too large', 'Moderate'),
    (100, 1, 10, 'Small displacement; low damping; fast oscillation', 'Moderate'),
    (100, 1, 100, 'Small-to-moderate displacement; slow but stiff response', 'Moderate'),
    (100, 10, 1, 'Very small displacement; moderate damping', 'Weak'),
    (100, 10, 10, 'Small displacement; moderate damping', 'Weak'),
    (100, 10, 100, 'Small displacement; moderate damping; slow response', 'Weak'),
    (100, 100, 1, 'Very small motion; heavy damping', 'Very weak'),
    (100, 100, 10, 'Very small displacement; strong damping', 'Very weak'),
    (100, 100, 100, 'Smallest response; strongest damping; slowest motion', 'Very weak'),
]

with PdfPages('kcm_effects_summary.pdf') as pdf:
    fig = plt.figure(figsize=(11, 8.5))
    fig.subplots_adjust(top=0.9, bottom=0.06, left=0.06, right=0.98)
    fig.text(
        0.05, 0.94,
        'How k, c and m affect the building response',
        fontsize=18, fontweight='bold'
    )
    text = (
        'The equation of motion is m u¨_b + c u˙_b + k u_b = c v_g + k u_g.\n\n'
        '- Increasing stiffness k reduces displacement and makes the building respond more quickly.\n'
        '- Decreasing k makes the structure softer, so displacements become larger.\n'
        '- Increasing damping c removes energy from the motion and suppresses oscillations.\n'
        '- Decreasing c allows the structure to oscillate for longer.\n'
        '- Increasing mass m makes the system heavier and slower, with a longer period.\n'
        '- Decreasing m makes the motion faster and more lively.\n\n'
        'Oscillations are strongest when damping is low and the system is not too stiff. '
        'The motion becomes more damped and less oscillatory as c increases, and it becomes '
        'more stable as k increases.'
    )
    fig.text(0.05, 0.68, text, fontsize=11, va='top', ha='left')

    table_rows = [['k', 'c', 'm', 'Expected response', 'Oscillation']] + [
        [str(k), str(c), str(m), rsp, osc] for k, c, m, rsp, osc in cases
    ]
    ax = fig.add_axes([0.04, 0.05, 0.92, 0.58])


    ax.axis('off')
    table = ax.table(
        cellText=table_rows[1:],
        colLabels=table_rows[0],
        loc='center',
        cellLoc='center',
        colWidths=[0.08, 0.08, 0.08, 0.58, 0.18],
    )
    table.auto_set_font_size(False)
    table.set_fontsize(7)
    table.scale(1, 1.8)
    pdf.savefig(fig)

    plt.close(fig)
