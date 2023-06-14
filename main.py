import mne
import json
import os
import matplotlib.pyplot as plt
import numpy as np
#workaround for -- _tkinter.TclError: invalid command name ".!canvas"
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Current path
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Load inputs from config.json
with open('config.json') as config_json:
    config = json.load(config_json)
tmp = dict((k, None) for k, v in config.items() if v == "")
config.update(tmp)

# Read the epoch file
data_file = config.pop('fif')
epochs = mne.read_epochs(data_file , preload=True)

evoked= epochs.average(config['picks'],config['method'], by_event_type=config['by_event_type'])

plt.figure(1)
if isinstance(evoked, list):
    titles = evoked[0].comment
    fig1 = evoked[0].plot(spatial_colors=True)
    fig1.text(0., 1., 'Evoked response for condition ' + titles + ' ... others in report.html', horizontalalignment='left', verticalalignment='top')
    titles = [ev.comment for ev in evoked]
else:
    titles = evoked.comment
    fig1 = evoked.plot(spatial_colors=True)
    fig1.text(0., 1., 'Evoked response for condition ' + titles, horizontalalignment='left', verticalalignment='top')

fig1.savefig(os.path.join('out_figs', 'evoked.png'))

    
report = mne.Report(title='ICA')
report.add_evokeds(evokeds=evoked, titles=titles)
report.save('out_report/report_evoked.html', overwrite=True)

mne.write_evokeds(os.path.join('out_dir', 'evokeds_ave.fif'), evoked, overwrite=True)

