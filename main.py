import mne
import json
import os
import matplotlib.pyplot as plt

# Current path
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

def epoch(raw,tmin,tmax):

    # extract an events array from Raw objects using mne.find_events():
    # reading experimental events from a “STIM” channel;
    events = mne.find_events(raw, stim_channel='STI 014')


    event_dict = {'auditory/left': 1, 'auditory/right': 2, 'visual/left': 3,
                  'visual/right': 4}

    epochs = mne.Epochs(raw, events, tmin=-0.3, tmax=0.7, event_id=event_dict,
                        preload=True)

    evoked = epochs['auditory/left'].average()
    evoked.plot()




    # == SAVE FILE ==
    evoked.save(os.path.join('out_dir', 'evoked-epo.fif'))

    # == FIGURES ==
    plt.figure()
    evoked.plot()
    plt.savefig(os.path.join('out_figs', 'voked_plot.png'))


    
 
    return epochs




def main():


    # Load inputs from config.json
    with open('config.json') as config_json:
        config = json.load(config_json)

    # Read the meg file
    data_file = config.pop('fif')

    # Read the event time
    tmin = config.pop('t_min')
    tmax = config.pop('t_max')

    # crop() the Raw data to save memory:
    raw = mne.io.read_raw_fif(data_file, verbose=False).crop(tmax=60)

    ## Build epochs parameters
    epochs_params = dict(tmin=tmin, tmax=tmax)

    epochs = epoch(raw,**epochs_params)







if __name__ == '__main__':
    main()
