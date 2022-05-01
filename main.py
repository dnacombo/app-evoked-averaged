import mne
import json
import os
import matplotlib.pyplot as plt

# Current path
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

def evoked(epochs):


    evoked = epochs.average()
    
    # == SAVE FILE ==
    evoked.save(os.path.join('out_dir', 'evoked-epo.fif'))

    # == FIGURES ==
    plt.figure()
    evoked.plot()
    plt.savefig(os.path.join('out_figs', 'evoked_plot.png'))


    
 
    return evoked




def main():


    # Load inputs from config.json
    with open('config.json') as config_json:
        config = json.load(config_json)

    # Read the epoch file
    data_file = config.pop('fif')


    # crop() the Raw data to save memory:
    epochs = mne.io.read_raw_fif(data_file, verbose=False).crop(tmax=60)

    evoked = evoked(epochs)


if __name__ == '__main__':
    main()
