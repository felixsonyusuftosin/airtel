



AIRTIME = 'AIRTIME'
DATA = 'DATA'
TALKTIME = 'TALKTIME'

notification_log_reader = open('input/notifications.log', 'r')
notification_log_airtime_writer = open('output/notifications_airtime.log', 'w')
notification_log_data_writer = open('output/notifications_data.log', 'w')
notification_log_talktime_writer = open('output/notifications_talktime.log', 'w')

for line in notification_log_reader:
  if AIRTIME in line:
     notification_log_airtime_writer.writelines([line])
  elif DATA in line:
     notification_log_data_writer.writelines([line])
  elif TALKTIME in line:
     notification_log_talktime_writer.writelines([line])
    
notification_log_reader.close()
notification_log_airtime_writer.close()
notification_log_data_writer.close()
notification_log_talktime_writer.close()


def print_airtime_logs():
    notification_log_airtime_reader = open('output/notifications_airtime.log', 'r')
    for line in notification_log_airtime_reader:
      print(line)
    notification_log_airtime_reader.close()
    

def print_data_logs():
    notification_log_data_reader = open('output/notifications_data.log', 'r')
    for line in notification_log_data_reader:
      print(line)
    notification_log_data_reader.close()

def print_talktime_logs():
  notification_log_talktime_reader = open('output/notifications_talktime.log', 'r')
  for line in notification_log_talktime_reader:
    print(line)
  notification_log_talktime_reader.close()


