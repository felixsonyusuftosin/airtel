import csv
import datetime
import math

AIRTIME_PURCHASE = 'AIRTIME_PURCHASE'
ACCOUNT_TRANSFERS = 'ACCOUNT_TRANSFERS'

def format_to_date(string_numbers):
   ''' Given the date format as described in the txt instructions we want to return a properly formated
      datetime object
   '''
   year = int(string_numbers[0:4])
   month = int(string_numbers[4:6])
   day = int(string_numbers[6:8])
   hour = int(string_numbers[8:10])
   minutes =int(string_numbers[10:12])
   seconds = int(string_numbers[12:14])
   date = datetime.datetime(year, month, day, hour, minutes, seconds)
   return date

def compute_date_difference_in_seconds(start_date, end_date):
  '''
   Given a datetime difference as datetime type we can compute the difference in seconds 
  '''
  difference = end_date - start_date
  return difference.seconds

def categorise_dialed_string(dialed_string):
   ''' Return the type of transaction '''
   list_of_individual_dialed_numbers = dialed_string.split('*')
   if not len(list_of_individual_dialed_numbers) > 1:
      return None
   last_element_index = len(list_of_individual_dialed_numbers) - 1
   last_element = list_of_individual_dialed_numbers[last_element_index]
   if len(str(last_element)) == 10:
      return ACCOUNT_TRANSFERS
   return AIRTIME_PURCHASE 
   

def get_session_time(difference_in_seconds):
   sessions = int(math.ceil(difference_in_seconds / 20))
   return sessions
   
def write_to_csv(row, test_file):
      test_writer = csv.writer(test_file, delimiter=',')
      test_writer.writerow(row)
     

with open('input/test_files.csv', newline='') as csv_file:
   with open('output/test_files_output.csv', 'w', newline='') as test_file:
      test_writer = csv.writer(test_file, delimiter=',')
      test_writer.writerow(['Short Code', 'Number of Sessions'])
      csv_reader = csv.reader(csv_file, delimiter=',')
      line_count = 0
      summary_dict = {'Account Transfers': 0, 'Airtime Purchase': 0}
      
      for row in csv_reader:
          start_date = str(row[2])
          end_date = str(row[3])
          short_code = row[4]
          dialed_string = row[5]

          start_date_date = format_to_date(start_date)
          end_date_date = format_to_date(end_date)
          diff = compute_date_difference_in_seconds(start_date_date, end_date_date)
          sessions = get_session_time(diff)
          row = [short_code, sessions]
          write_to_csv(row, test_file)
          category_of_transfer = categorise_dialed_string(dialed_string)
          
          if category_of_transfer == ACCOUNT_TRANSFERS:
            summary_dict['Account Transfers'] = summary_dict['Account Transfers'] + 1
          elif category_of_transfer == AIRTIME_PURCHASE:
            summary_dict['Airtime Purchase'] = summary_dict['Airtime Purchase'] + 1
         
      with open('output/test_files_summary.csv', 'w', newline='') as summary_file:
        summary_writer = csv.writer(summary_file, delimiter=',')
        summary_writer.writerow(['Account Transfers', 'Airtime Purchase'])
        summary_writer.writerow([summary_dict['Account Transfers'], summary_dict['Airtime Purchase']])

                  
