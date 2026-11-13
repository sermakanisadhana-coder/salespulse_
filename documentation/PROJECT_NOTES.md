# Project Notes

## Project
DIT-P05 – Sales Report Automation

## Business problem
Manual sales calculations and report preparation can take time and may lead to errors.

## Solution
A web interface accepts sales data and automates validation, achievement analysis, report generation and dashboard display.

## Input
Employee_ID, Employee_Name, Target, Achieved, Region

## Outputs
- Processed sales report
- Summary worksheet
- Rejected-row worksheet
- Separate error report
- Website dashboard
- Application error log

## Assessment rule clarification
The team brief lists Employee_ID, Employee_Name, Target, Achieved and Region as inputs. Its incentive example calculates incentive from salary, but Salary is not listed in the input schema. The application therefore calculates and displays the incentive rate only. Ask the project mentor whether a Salary column should be added before calculating incentive payout amounts.
