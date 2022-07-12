import mne
import json
import os
import matplotlib.pyplot as plt

# Current path
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


def evoked(epochs):
    
    e1 = epochs[1].average()
    evokeds_subset=e1
    evokeds_subset.pick('meg')
    report = mne.Report(title='Evoked example')
    report.add_evokeds(
        evokeds=evokeds_subset,
        titles=['evoked 1' # Manually specify titles
                ],
        n_time_points=5
    )
    
      # == SAVE REPORT ==
    report.save('out_dir_report/report.html', overwrite=True)
    # == SAVE FILE ==
    evokeds.save(os.path.join('out_dir', 'evoked-epo.fif'))

    return evokeds


def main():
    # Load inputs from config.json
    with open('config.json') as config_json:
        config = json.load(config_json)

    # Read the epoch file
    data_file = config.pop('fif')
    epochs = mne.read_epochs(data_file , preload=False)
    evok = evoked(epochs)

if __name__ == '__main__':
    main()


