import os
import random
import pathlib
import subprocess

def create_training_data(input_file, font, output_directory, count=1000):
    lines = []

    with open(input_file, 'r') as input_file:
        for line in input_file.readlines():
            lines.append(line.strip())

    if not os.path.exists(output_directory):
        os.mkdir(output_directory)

    lines = lines[:count]

    line_count = 0
    for line in lines:
        training_text_file_name = pathlib.Path(input_file.name).stem
        line_training_text = os.path.join(output_directory, f'{training_text_file_name}_{line_count}.gt.txt')
        with open(line_training_text, 'w') as output_file:
            output_file.writelines([line])

        file_base_name = f'{training_text_file_name}_{line_count}'

        subprocess.run([
            'text2image',
            f'--font={font}',
            f'--text={line_training_text}',
            f'--outputbase={output_directory}/{file_base_name}',
            '--max_pages=1',
            '--strip_unrenderable_words',
            '--leading=32',
            '--xsize=3600',
            '--ysize=480',
            '--char_spacing=0.1',
            '--exposure=0',
            '--unicharset_file=tesstrain/data/langdata/Arabic.unicharset'
        ])

        line_count += 1

# Example usage:

create_training_data('low_diacritics_evaluation/a.txt', 'AlArabiya', 'tesstrain/data/low_diacritics_evaluation-ground-truth')
create_training_data('low_diacritics_evaluation/b.txt', 'AlBattar', 'tesstrain/data/low_diacritics_evaluation-ground-truth')
create_training_data('low_diacritics_evaluation/c.txt', 'AlHor', 'tesstrain/data/low_diacritics_evaluation-ground-truth')
create_training_data('low_diacritics_evaluation/d.txt', 'AlManzomah', 'tesstrain/data/low_diacritics_evaluation-ground-truth')
create_training_data('low_diacritics_evaluation/e.txt', 'AlYarmook', 'tesstrain/data/low_diacritics_evaluation-ground-truth')
create_training_data('low_diacritics_evaluation/f.txt', 'Arab', 'tesstrain/data/low_diacritics_evaluation-ground-truth')
create_training_data('low_diacritics_evaluation/g.txt', 'Cortoba', 'tesstrain/data/low_diacritics_evaluation-ground-truth')
create_training_data('low_diacritics_evaluation/h.txt', 'DejaVu Sans', 'tesstrain/data/low_diacritics_evaluation-ground-truth')
create_training_data('low_diacritics_evaluation/i.txt', 'DejaVu Sans Mono', 'tesstrain/data/low_diacritics_evaluation-ground-truth')
create_training_data('low_diacritics_evaluation/j.txt', 'Dimnah', 'tesstrain/data/low_diacritics_evaluation-ground-truth')
create_training_data('low_diacritics_evaluation/k.txt', 'Electron', 'tesstrain/data/low_diacritics_evaluation-ground-truth')
create_training_data('low_diacritics_evaluation/l.txt', 'Furat', 'tesstrain/data/low_diacritics_evaluation-ground-truth')
create_training_data('low_diacritics_evaluation/m.txt', 'Granada', 'tesstrain/data/low_diacritics_evaluation-ground-truth')
create_training_data('low_diacritics_evaluation/n.txt', 'Graph', 'tesstrain/data/low_diacritics_evaluation-ground-truth')
create_training_data('low_diacritics_evaluation/o.txt', 'Hani', 'tesstrain/data/low_diacritics_evaluation-ground-truth')
create_training_data('low_diacritics_evaluation/p.txt', 'Hor', 'tesstrain/data/low_diacritics_evaluation-ground-truth')
create_training_data('low_diacritics_evaluation/q.txt', 'Japan', 'tesstrain/data/low_diacritics_evaluation-ground-truth')
create_training_data('low_diacritics_evaluation/r.txt', 'Jet', 'tesstrain/data/low_diacritics_evaluation-ground-truth')
create_training_data('low_diacritics_evaluation/s.txt', 'Kayrawan', 'tesstrain/data/low_diacritics_evaluation-ground-truth')
create_training_data('low_diacritics_evaluation/t.txt', 'Khalid', 'tesstrain/data/low_diacritics_evaluation-ground-truth')
create_training_data('low_diacritics_evaluation/u.txt', 'Mashq', 'tesstrain/data/low_diacritics_evaluation-ground-truth')
create_training_data('low_diacritics_evaluation/v.txt', 'Metal', 'tesstrain/data/low_diacritics_evaluation-ground-truth')
create_training_data('low_diacritics_evaluation/w.txt', 'Nada', 'tesstrain/data/low_diacritics_evaluation-ground-truth')
create_training_data('low_diacritics_evaluation/x.txt', 'Nagham', 'tesstrain/data/low_diacritics_evaluation-ground-truth')
create_training_data('low_diacritics_evaluation/y.txt', 'Nice', 'tesstrain/data/low_diacritics_evaluation-ground-truth')
create_training_data('low_diacritics_evaluation/z.txt', 'Ostorah', 'tesstrain/data/low_diacritics_evaluation-ground-truth')
create_training_data('low_diacritics_evaluation/aa.txt', 'Petra', 'tesstrain/data/low_diacritics_evaluation-ground-truth')
create_training_data('low_diacritics_evaluation/ab.txt', 'Rehan', 'tesstrain/data/low_diacritics_evaluation-ground-truth')
create_training_data('low_diacritics_evaluation/ac.txt', 'Salem', 'tesstrain/data/low_diacritics_evaluation-ground-truth')
create_training_data('low_diacritics_evaluation/ad.txt', 'Shado', 'tesstrain/data/low_diacritics_evaluation-ground-truth')
create_training_data('low_diacritics_evaluation/ae.txt', 'Sharjah', 'tesstrain/data/low_diacritics_evaluation-ground-truth')
create_training_data('low_diacritics_evaluation/af.txt', 'Sindbad', 'tesstrain/data/low_diacritics_evaluation-ground-truth')
create_training_data('low_diacritics_evaluation/ag.txt', 'Tarablus', 'tesstrain/data/low_diacritics_evaluation-ground-truth')
create_training_data('low_diacritics_evaluation/ah.txt', 'Tholoth', 'tesstrain/data/low_diacritics_evaluation-ground-truth')

create_training_data('mid_diacritics_evaluation/a.txt', 'AlArabiya', 'tesstrain/data/mid_diacritics_evaluation-ground-truth')
create_training_data('mid_diacritics_evaluation/b.txt', 'AlBattar', 'tesstrain/data/mid_diacritics_evaluation-ground-truth')
create_training_data('mid_diacritics_evaluation/c.txt', 'AlHor', 'tesstrain/data/mid_diacritics_evaluation-ground-truth')
create_training_data('mid_diacritics_evaluation/d.txt', 'AlManzomah', 'tesstrain/data/mid_diacritics_evaluation-ground-truth')
create_training_data('mid_diacritics_evaluation/e.txt', 'AlYarmook', 'tesstrain/data/mid_diacritics_evaluation-ground-truth')
create_training_data('mid_diacritics_evaluation/f.txt', 'Arab', 'tesstrain/data/mid_diacritics_evaluation-ground-truth')
create_training_data('mid_diacritics_evaluation/g.txt', 'Cortoba', 'tesstrain/data/mid_diacritics_evaluation-ground-truth')
create_training_data('mid_diacritics_evaluation/h.txt', 'DejaVu Sans', 'tesstrain/data/mid_diacritics_evaluation-ground-truth')
create_training_data('mid_diacritics_evaluation/i.txt', 'DejaVu Sans Mono', 'tesstrain/data/mid_diacritics_evaluation-ground-truth')
create_training_data('mid_diacritics_evaluation/j.txt', 'Dimnah', 'tesstrain/data/mid_diacritics_evaluation-ground-truth')
create_training_data('mid_diacritics_evaluation/k.txt', 'Electron', 'tesstrain/data/mid_diacritics_evaluation-ground-truth')
create_training_data('mid_diacritics_evaluation/l.txt', 'Furat', 'tesstrain/data/mid_diacritics_evaluation-ground-truth')
create_training_data('mid_diacritics_evaluation/m.txt', 'Granada', 'tesstrain/data/mid_diacritics_evaluation-ground-truth')
create_training_data('mid_diacritics_evaluation/n.txt', 'Graph', 'tesstrain/data/mid_diacritics_evaluation-ground-truth')
create_training_data('mid_diacritics_evaluation/o.txt', 'Hani', 'tesstrain/data/mid_diacritics_evaluation-ground-truth')
create_training_data('mid_diacritics_evaluation/p.txt', 'Hor', 'tesstrain/data/mid_diacritics_evaluation-ground-truth')
create_training_data('mid_diacritics_evaluation/q.txt', 'Japan', 'tesstrain/data/mid_diacritics_evaluation-ground-truth')
create_training_data('mid_diacritics_evaluation/r.txt', 'Jet', 'tesstrain/data/mid_diacritics_evaluation-ground-truth')
create_training_data('mid_diacritics_evaluation/s.txt', 'Kayrawan', 'tesstrain/data/mid_diacritics_evaluation-ground-truth')
create_training_data('mid_diacritics_evaluation/t.txt', 'Khalid', 'tesstrain/data/mid_diacritics_evaluation-ground-truth')
create_training_data('mid_diacritics_evaluation/u.txt', 'Mashq', 'tesstrain/data/mid_diacritics_evaluation-ground-truth')
create_training_data('mid_diacritics_evaluation/v.txt', 'Metal', 'tesstrain/data/mid_diacritics_evaluation-ground-truth')
create_training_data('mid_diacritics_evaluation/w.txt', 'Nada', 'tesstrain/data/mid_diacritics_evaluation-ground-truth')
create_training_data('mid_diacritics_evaluation/x.txt', 'Nagham', 'tesstrain/data/mid_diacritics_evaluation-ground-truth')
create_training_data('mid_diacritics_evaluation/y.txt', 'Nice', 'tesstrain/data/mid_diacritics_evaluation-ground-truth')
create_training_data('mid_diacritics_evaluation/z.txt', 'Ostorah', 'tesstrain/data/mid_diacritics_evaluation-ground-truth')
create_training_data('mid_diacritics_evaluation/aa.txt', 'Petra', 'tesstrain/data/mid_diacritics_evaluation-ground-truth')
create_training_data('mid_diacritics_evaluation/ab.txt', 'Rehan', 'tesstrain/data/mid_diacritics_evaluation-ground-truth')
create_training_data('mid_diacritics_evaluation/ac.txt', 'Salem', 'tesstrain/data/mid_diacritics_evaluation-ground-truth')
create_training_data('mid_diacritics_evaluation/ad.txt', 'Shado', 'tesstrain/data/mid_diacritics_evaluation-ground-truth')
create_training_data('mid_diacritics_evaluation/ae.txt', 'Sharjah', 'tesstrain/data/mid_diacritics_evaluation-ground-truth')
create_training_data('mid_diacritics_evaluation/af.txt', 'Sindbad', 'tesstrain/data/mid_diacritics_evaluation-ground-truth')
create_training_data('mid_diacritics_evaluation/ag.txt', 'Tarablus', 'tesstrain/data/mid_diacritics_evaluation-ground-truth')
create_training_data('mid_diacritics_evaluation/ah.txt', 'Tholoth', 'tesstrain/data/mid_diacritics_evaluation-ground-truth')

create_training_data('high_diacritics_evaluation/a.txt', 'AlArabiya', 'tesstrain/data/high_diacritics_evaluation-ground-truth')
create_training_data('high_diacritics_evaluation/b.txt', 'AlBattar', 'tesstrain/data/high_diacritics_evaluation-ground-truth')
create_training_data('high_diacritics_evaluation/c.txt', 'AlHor', 'tesstrain/data/high_diacritics_evaluation-ground-truth')
create_training_data('high_diacritics_evaluation/d.txt', 'AlManzomah', 'tesstrain/data/high_diacritics_evaluation-ground-truth')
create_training_data('high_diacritics_evaluation/e.txt', 'AlYarmook', 'tesstrain/data/high_diacritics_evaluation-ground-truth')
create_training_data('high_diacritics_evaluation/f.txt', 'Arab', 'tesstrain/data/high_diacritics_evaluation-ground-truth')
create_training_data('high_diacritics_evaluation/g.txt', 'Cortoba', 'tesstrain/data/high_diacritics_evaluation-ground-truth')
create_training_data('high_diacritics_evaluation/h.txt', 'DejaVu Sans', 'tesstrain/data/high_diacritics_evaluation-ground-truth')
create_training_data('high_diacritics_evaluation/i.txt', 'DejaVu Sans Mono', 'tesstrain/data/high_diacritics_evaluation-ground-truth')
create_training_data('high_diacritics_evaluation/j.txt', 'Dimnah', 'tesstrain/data/high_diacritics_evaluation-ground-truth')
create_training_data('high_diacritics_evaluation/k.txt', 'Electron', 'tesstrain/data/high_diacritics_evaluation-ground-truth')
create_training_data('high_diacritics_evaluation/l.txt', 'Furat', 'tesstrain/data/high_diacritics_evaluation-ground-truth')
create_training_data('high_diacritics_evaluation/m.txt', 'Granada', 'tesstrain/data/high_diacritics_evaluation-ground-truth')
create_training_data('high_diacritics_evaluation/n.txt', 'Graph', 'tesstrain/data/high_diacritics_evaluation-ground-truth')
create_training_data('high_diacritics_evaluation/o.txt', 'Hani', 'tesstrain/data/high_diacritics_evaluation-ground-truth')
create_training_data('high_diacritics_evaluation/p.txt', 'Hor', 'tesstrain/data/high_diacritics_evaluation-ground-truth')
create_training_data('high_diacritics_evaluation/q.txt', 'Japan', 'tesstrain/data/high_diacritics_evaluation-ground-truth')
create_training_data('high_diacritics_evaluation/r.txt', 'Jet', 'tesstrain/data/high_diacritics_evaluation-ground-truth')
create_training_data('high_diacritics_evaluation/s.txt', 'Kayrawan', 'tesstrain/data/high_diacritics_evaluation-ground-truth')
create_training_data('high_diacritics_evaluation/t.txt', 'Khalid', 'tesstrain/data/high_diacritics_evaluation-ground-truth')
create_training_data('high_diacritics_evaluation/u.txt', 'Mashq', 'tesstrain/data/high_diacritics_evaluation-ground-truth')
create_training_data('high_diacritics_evaluation/v.txt', 'Metal', 'tesstrain/data/high_diacritics_evaluation-ground-truth')
create_training_data('high_diacritics_evaluation/w.txt', 'Nada', 'tesstrain/data/high_diacritics_evaluation-ground-truth')
create_training_data('high_diacritics_evaluation/x.txt', 'Nagham', 'tesstrain/data/high_diacritics_evaluation-ground-truth')
create_training_data('high_diacritics_evaluation/y.txt', 'Nice', 'tesstrain/data/high_diacritics_evaluation-ground-truth')
create_training_data('high_diacritics_evaluation/z.txt', 'Ostorah', 'tesstrain/data/high_diacritics_evaluation-ground-truth')
create_training_data('high_diacritics_evaluation/aa.txt', 'Petra', 'tesstrain/data/high_diacritics_evaluation-ground-truth')
create_training_data('high_diacritics_evaluation/ab.txt', 'Rehan', 'tesstrain/data/high_diacritics_evaluation-ground-truth')
create_training_data('high_diacritics_evaluation/ac.txt', 'Salem', 'tesstrain/data/high_diacritics_evaluation-ground-truth')
create_training_data('high_diacritics_evaluation/ad.txt', 'Shado', 'tesstrain/data/high_diacritics_evaluation-ground-truth')
create_training_data('high_diacritics_evaluation/ae.txt', 'Sharjah', 'tesstrain/data/high_diacritics_evaluation-ground-truth')
create_training_data('high_diacritics_evaluation/af.txt', 'Sindbad', 'tesstrain/data/high_diacritics_evaluation-ground-truth')
create_training_data('high_diacritics_evaluation/ag.txt', 'Tarablus', 'tesstrain/data/high_diacritics_evaluation-ground-truth')
create_training_data('high_diacritics_evaluation/ah.txt', 'Tholoth', 'tesstrain/data/high_diacritics_evaluation-ground-truth')

# create_training_data('high_diacritics_evaluation/AlArabiya.txt', 'AlArabiya', 'tesstrain/data/high_diacritics_evaluation-ground-truth')
# create_training_data('high_diacritics_evaluation/AlBattar.txt', 'AlBattar', 'tesstrain/data/high_diacritics_evaluation-ground-truth')
# create_training_data('high_diacritics_evaluation/AlHor.txt', 'AlHor', 'tesstrain/data/high_diacritics_evaluation-ground-truth')
# create_training_data('high_diacritics_evaluation/AlManzomah.txt', 'AlManzomah', 'tesstrain/data/high_diacritics_evaluation-ground-truth')
# create_training_data('high_diacritics_evaluation/AlYarmook.txt', 'AlYarmook', 'tesstrain/data/high_diacritics_evaluation-ground-truth')
# create_training_data('high_diacritics_evaluation/Arab.txt', 'Arab', 'tesstrain/data/high_diacritics_evaluation-ground-truth')
# create_training_data('high_diacritics_evaluation/Cortoba.txt', 'Cortoba', 'tesstrain/data/high_diacritics_evaluation-ground-truth')
# create_training_data('high_diacritics_evaluation/DejaVuSans.txt', 'DejaVu Sans', 'tesstrain/data/high_diacritics_evaluation-ground-truth')
# create_training_data('high_diacritics_evaluation/DejaVuSansMono.txt', 'DejaVu Sans Mono', 'tesstrain/data/high_diacritics_evaluation-ground-truth')
# create_training_data('high_diacritics_evaluation/Dimnah.txt', 'Dimnah', 'tesstrain/data/high_diacritics_evaluation-ground-truth')
# create_training_data('high_diacritics_evaluation/Electron.txt', 'Electron', 'tesstrain/data/high_diacritics_evaluation-ground-truth')
# create_training_data('high_diacritics_evaluation/Furat.txt', 'Furat', 'tesstrain/data/high_diacritics_evaluation-ground-truth')
# create_training_data('high_diacritics_evaluation/Granada.txt', 'Granada', 'tesstrain/data/high_diacritics_evaluation-ground-truth')
# create_training_data('high_diacritics_evaluation/Graph.txt', 'Graph', 'tesstrain/data/high_diacritics_evaluation-ground-truth')
# create_training_data('high_diacritics_evaluation/Hani.txt', 'Hani', 'tesstrain/data/high_diacritics_evaluation-ground-truth')
# create_training_data('high_diacritics_evaluation/Hor.txt', 'Hor', 'tesstrain/data/high_diacritics_evaluation-ground-truth')
# create_training_data('high_diacritics_evaluation/Japan.txt', 'Japan', 'tesstrain/data/high_diacritics_evaluation-ground-truth')
# create_training_data('high_diacritics_evaluation/Jet.txt', 'Jet', 'tesstrain/data/high_diacritics_evaluation-ground-truth')
# create_training_data('high_diacritics_evaluation/Kayrawan.txt', 'Kayrawan', 'tesstrain/data/high_diacritics_evaluation-ground-truth')
# create_training_data('high_diacritics_evaluation/Khalid.txt', 'Khalid', 'tesstrain/data/high_diacritics_evaluation-ground-truth')
# create_training_data('high_diacritics_evaluation/Mashq.txt', 'Mashq', 'tesstrain/data/high_diacritics_evaluation-ground-truth')
# create_training_data('high_diacritics_evaluation/Metal.txt', 'Metal', 'tesstrain/data/high_diacritics_evaluation-ground-truth')
# create_training_data('high_diacritics_evaluation/Nada.txt', 'Nada', 'tesstrain/data/high_diacritics_evaluation-ground-truth')
# create_training_data('high_diacritics_evaluation/Nagham.txt', 'Nagham', 'tesstrain/data/high_diacritics_evaluation-ground-truth')
# create_training_data('high_diacritics_evaluation/Nice.txt', 'Nice', 'tesstrain/data/high_diacritics_evaluation-ground-truth')
# create_training_data('high_diacritics_evaluation/Ostorah.txt', 'Ostorah', 'tesstrain/data/high_diacritics_evaluation-ground-truth')
# create_training_data('high_diacritics_evaluation/Petra.txt', 'Petra', 'tesstrain/data/high_diacritics_evaluation-ground-truth')
# create_training_data('high_diacritics_evaluation/Rehan.txt', 'Rehan', 'tesstrain/data/high_diacritics_evaluation-ground-truth')
# create_training_data('high_diacritics_evaluation/Salem.txt', 'Salem', 'tesstrain/data/high_diacritics_evaluation-ground-truth')
# create_training_data('high_diacritics_evaluation/Shado.txt', 'Shado', 'tesstrain/data/high_diacritics_evaluation-ground-truth')
# create_training_data('high_diacritics_evaluation/Sharjah.txt', 'Sharjah', 'tesstrain/data/high_diacritics_evaluation-ground-truth')
# create_training_data('high_diacritics_evaluation/Sindbad.txt', 'Sindbad', 'tesstrain/data/high_diacritics_evaluation-ground-truth')
# create_training_data('high_diacritics_evaluation/Tarablus.txt', 'Tarablus', 'tesstrain/data/high_diacritics_evaluation-ground-truth')
# create_training_data('high_diacritics_evaluation/Tholoth.txt', 'Tholoth', 'tesstrain/data/high_diacritics_evaluation-ground-truth')