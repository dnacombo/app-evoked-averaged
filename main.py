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


def evoked(epochs, ch_type):

    evoked= epochs.average()


    plt.figure(1)
    fig1=evoked.plot(spatial_colors=True)
    fig1.savefig(os.path.join('out_figs', 'evoke.png'))
    
    times = np.arange(timepoints_from, timepoints_to, step)

    plt.figure(2)
    fig2=evoked.plot_topomap(times , ch_type=ch_type)
    fig2.savefig(os.path.join('out_figs', 'evoketopo.png'))


    plt.figure(3)
    fig3=evoked.plot_joint(times, picks=ch_type)
    fig3.savefig(os.path.join('out_figs', 'evokejoint.png'))
    
    mne.write_evokeds(os.path.join('out_dir', 'evokeds_ave.fif'), evoked, overwrite=True)
    

def main():
    # Load inputs from config.json
    with open('config.json') as config_json:
        config = json.load(config_json)

    # Read the epoch file
    data_file = config.pop('fif')
    epochs = mne.read_epochs(data_file , preload=False)
    evok = evoked(epochs,config['ch_type'],config['timepoints_from'], config['timepoints_to'], config['step'])

if __name__ == '__main__':
    main()


