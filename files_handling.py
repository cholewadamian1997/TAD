import pandas as pd
import os

CURRENT_DIRECTORY = os.getcwd()

# Files names:
AI_PATENTS = pd.read_excel("Data/artificial_inteligence_patents_aplications.xlsx")
LIDAR_PATENTS = pd.read_excel("Data/owners_of_LIDAR_patents.xlsx")
AUTONOMOUS_DRIVING_PATENT = pd.read_excel("Data/autonomous_driving_patent_owners.xlsx")
VISION_MARKET_SIZE_CHINA = pd.read_excel("Data/vision_industry_market_size_in_china.xlsx")
VISION_MARKET_SIZE_USA = pd.read_excel("Data/machine_vision_market_usa.xlsx")
VISION_MARKET_SIZE_IN_MEDICINE = pd.read_excel("Data/computer_vision_ai_market_revenue_medicine.xlsx")
FOUNDING_AI_STARTUPS_ISRAEL = pd.read_excel("Data/funding_of_ai-startups_israel.xlsx")
FOUNDING_AI_STARTUPS_WORLD = pd.read_excel("Data/funding_of_ai-startups_worldwide.xlsx")
SENSORS_GT = pd.read_csv('Data/sensors.csv')
VISUAL_SYSTEMS_GT = pd.read_csv('Data/visual_systems.csv')
VISION_MARKET_SIZE_WORLDWIDE = pd.read_excel('Data/vision_industry_market_size_worldwide.xlsx')
AUTONOMOUS_DRIVING_PATENT_COMPANIES = pd.read_excel('Data/companies_with most_autonomus_drivin_patensts.xlsx')



""" Wyświetlanie jak wyglądają dane

print(LIDAR_PATENTS.head())
print(AUTONOMOUS_DRIVING_PATENT.head())
print(VISION_MARKET_SIZE_CHINA.head())
print(VISION_MARKET_SIZE_USA.head())
print(VISION_MARKET_SIZE_IN_MEDICINE.head())
print(FOUNDING_AI_STARTUPS_ISRAEL.head())
print(FOUNDING_AI_STARTUPS_WORLD.head())"""
print(AI_PATENTS.head())

