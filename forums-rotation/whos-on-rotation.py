import os
import datetime
import pprint

import slack


TODAY = datetime.date.today()
NOTIFICATION = (
    '*Forums Rotations for the week of {date}* :tada:\n'
    '\n'
    'Just a friendly reminder that {name} is on forums support '
    'rotation this week! For the full rotations schedule, take a look at the '
    'list https://github.com/natcap/softwareteam.'
)


def whos_on_rotation_today():
    """Determine who's on rotation today and send a slack message.

    This program assumes that a file, ``rotations.txt`` exists in the same
    directory as this file, and that the file contains lines like so::

        2020-02-24 James

    Each line must have one date in the format year-month-day and a name, with
    the two values separated by a space.  The file must also be in sorted
    order, with later dates being listed farther down the file.

    This program assumes that it will run on the dates listed in the file.

    Returns:
        ``None``.

    """
    rotations_filepath = os.path.join(
        os.path.dirname(__file__), 'rotations.txt')

    with open(rotations_filepath) as rotations:
        for line in rotations:
            date_string, name = line.rstrip().split(' ')
            date = datetime.datetime.strptime(date_string, '%Y-%m-%d').date()

            if date < TODAY:
                continue

            elif date == TODAY:
                client = slack.WebClient(token=os.environ['SLACK_API_TOKEN'])

                client.chat_postMessage(
                    channel='#softwareteam',
                    mrkdwn=True,
                    link_names=True,
                    parse='full',
                    unfurl_media=False,
                    text=NOTIFICATION.format(
                        date=TODAY.strftime('%B %d, %Y'),
                        name=whos_on_rotation)
                )
                return None

            else:
                raise AssertionError(
                    'This program is running on a schedule that is '
                    'out-of-sync with the dates in rotations.txt. Both should '
                    'refer to Mondays.')

        raise ValueError(
            'We need to add more forums assignments to rotations.txt!')


if __name__ == '__main__':
    whos_on_rotation_today()
