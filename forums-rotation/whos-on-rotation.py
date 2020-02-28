import os
import datetime

import slack


TODAY = datetime.date.today()
NOTIFICATION = """*Forums Rotations for the week of {date}* :tada:

Just a friendly reminder that <{username}> is on forums support rotation
this week! For the full rotations schedule, take a look at the list
https://github.com/natcap/softwareteam.
"""

# TODO: message a person directly (see:
#     https://stackoverflow.com/a/36463098/299084)
# TODO: GH Actions cron
# TODO: Document the OAuth scopes required to make this bot happen
# TODO: test this on my own direct channel if at all possible so I don't spam
#     #softwareteam

def whos_on_rotation_today():
    with open('rotations.txt') as rotations:
        for line in rotations:
            date_string, slack_user_string = line.rstrip().split(' ')
            date = datetime.datetime.strptime(date_string, '%Y-%m-%d').date()
            print(date, TODAY)
            if date < TODAY:
                if TODAY - datetime.timedelta(weeks=1) < date:
                    print('Today is not an alert day, but %s is on rotation.' %
                          slack_user_string)
                    return None
                else:
                    print('%s has already passed' % date_string)
                    continue
            elif date == TODAY:
                print('Today is an alert day and %s is on rotation!' %
                      slack_user_string)
                return slack_user_string
            else:
                return None


def send_slack_message(whos_on_rotation):
    client = slack.WebClient(token=os.environ['SLACK_API_TOKEN'])
    client.chat_postMessage(
        channel='softwareteam',
        link_names=True,
        text=NOTIFICATION.format(
            date=TODAY.strftime('%B %d, %Y'),
            username=whos_on_rotation)
    )


def main():
    whos_on_rotation = whos_on_rotation_today()
    if whos_on_rotation:
        send_slack_message(whos_on_rotation)


if __name__ == '__main__':
    main()
