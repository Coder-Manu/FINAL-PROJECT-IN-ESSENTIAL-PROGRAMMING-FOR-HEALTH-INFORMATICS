import pandas as pd
import matplotlib.pyplot as plt
import hashlib
from datetime import datetime


class PatientRecord:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data_frame = self.load_data(file_path)

    @staticmethod
    def load_data(file_path):
        try:
            return pd.read_csv(file_path, parse_dates=['Visit_time'])
        except FileNotFoundError:
            print("Patient data file not found.")
            return pd.DataFrame()
        except Exception as e:
            print(f"Error reading patient data: {e}")
            return pd.DataFrame()

    def add_patient_record(self, patient_information):
        patient_information['Visit_time'] = pd.to_datetime(
            patient_information['Visit_time'])
        patient_id = str(patient_information['Patient_ID'])

        # Create a DataFrame for the new patient record
        new_record_df = pd.DataFrame([patient_information])

        # Use concat instead of append
        self.data_frame = pd.concat(
            [self.data_frame, new_record_df], ignore_index=True)

        # Save changes to the CSV file
        self.data_frame.to_csv(self.file_path, index=False)

    def delete_patient_record(self, patient_id):
        patient_id = str(patient_id)
        if patient_id in self.data_frame['Patient_ID'].astype(str).values:
            self.data_frame = self.data_frame[self.data_frame['Patient_ID'].astype(
                str) != patient_id]
            print(f"Deleted records for patient ID {patient_id}")
            # Save changes to the CSV file
            self.data_frame.to_csv(self.file_path, index=False)
            return True
        else:
            print("Patient ID not found. No records were erased.")
            return False

    def retrieve_visit(self, patient_id):
        patient_id = str(patient_id)
        results = self.data_frame[self.data_frame['Patient_ID'].astype(
            str) == patient_id]
        if not results.empty:
            return results
        else:
            print("Patient ID not found.")
            return pd.DataFrame()

    def count_visits(self, date):
        try:
            target_date = pd.to_datetime(date).date()
            self.data_frame['Visit_time'] = pd.to_datetime(
                self.data_frame['Visit_time'])
            count = (
                self.data_frame['Visit_time'].dt.date == target_date).sum()
            print(f"Total visits on {date}: {count}")
            return count
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

    def generate_statistics(self):
        print("Generating statistics for management...")
        self.data_frame['Visit_time'] = pd.to_datetime(
            self.data_frame['Visit_time'])

        # Visits Over Time (Monthly)
        visits_over_time = self.data_frame['Visit_time'].dt.to_period(
            'M').value_counts().sort_index()
        visits_over_time.plot(kind='line', title='Visits Over Time (Monthly)')
        plt.xlabel('Month')
        plt.ylabel('Number of Visits')
        plt.show()

        # Visit Counts by Department
        self.data_frame['Visit_department'].value_counts().plot(
            kind='bar', title='Visit Counts by Department')
        plt.xlabel('Department')
        plt.ylabel('Number of Visits')
        plt.show()

        # Visit Counts by Insurance Type
        self.data_frame['Insurance'].value_counts().plot(
            kind='pie', title='Visit Counts by Insurance Type', autopct='%1.1f%%')
        plt.ylabel('')  # Hide the y-label as it's unnecessary for pie charts
        plt.show()

        # Demographic Breakdown by Race and Gender
        self.data_frame.groupby(['Race', 'Gender']).size().unstack().plot(
            kind='bar', stacked=True, title='Demographic Breakdown')
        plt.xlabel('Race')
        plt.ylabel('Number of Visits')
        plt.show()

        # Age Distribution of Patients
        self.data_frame['Age'].plot(
            kind='hist', bins=20, title='Age Distribution of Patients')
        plt.xlabel('Age')
        plt.ylabel('Frequency')
        plt.show()

        # Chief Complaint Analysis
        top_complaints = self.data_frame['Chief_complaint'].value_counts().head(
            10)
        top_complaints.plot(kind='bar', title='Top 10 Chief Complaints')
        plt.xlabel('Chief Complaint')
        plt.ylabel('Number of Occurrences')
        plt.show()

        # Visits by Day of the Week
        self.data_frame['day_of_week'] = self.data_frame['Visit_time'].dt.day_name()
        visits_by_day = self.data_frame['day_of_week'].value_counts()
        visits_by_day.plot(kind='bar', title='Visits by Day of the Week')
        plt.xlabel('Day of the Week')
        plt.ylabel('Number of Visits')
        plt.show()
