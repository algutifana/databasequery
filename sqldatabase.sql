CREATE VIEW EmployeesPerRegion AS
SELECT r.region_name, COUNT(e.employee_id) AS "Number of Employees"
FROM regions r 
JOIN countries c on c.region_id = r.region_id 
JOIN locations l on l.country_id = c.country_id 
JOIN departments d on d.location_id = l.location_id 
JOIN employees e on e.department_id = d.department_id
GROUP BY r.region_name;

SELECT * FROM EmployeesPerRegion
WHERE region_name = "Americas";


CREATE VIEW managers AS 
SELECT e2.first_name, e2.last_name, e2.phone_number, e2.email, j.job_title, d.department_name
FROM employees e1
JOIN employees e2 on e2.employee_id = e1.manager_id 
JOIN jobs j on j.job_id = e2.job_id 
JOIN departments d on d.department_id = e2.department_id;

SELECT department_name, COUNT(department_name) 
FROM managers 
GROUP BY department_name;

CREATE VIEW DependentsByDepartment AS 
SELECT d.department_name, COUNT(dt.dependent_id) AS dependents
FROM departments d 
JOIN employees e on e.department_id = d.department_id 
JOIN dependents dt on dt.employee_id = e.employee_id
GROUP BY d.department_name;


SELECT * FROM DependentsByDepartment
ORDER BY dependents DESC
LIMIT 1;


CREATE VIEW HiresByYear AS 
SELECT YEAR(hire_date) AS yearhired, COUNT(employee_id)
FROM employees
GROUP BY yearhired;

SELECT * FROM HiresByYear
WHERE yearhired = 1997;


CREATE VIEW SalaryByDepartment AS 
SELECT d.department_name, SUM(e.salary) AS totalsalary
FROM departments d 
JOIN employees e on e.department_id = d.department_id
GROUP BY d.department_name;

SELECT * FROM SalaryByDepartment 
WHERE department_name = "Finance";


CREATE VIEW SalaryByJobTitle AS 
SELECT j.job_title, SUM(e.salary) AS totalsalary 
FROM jobs j 
JOIN employees e on e.job_id = j.job_id
GROUP BY j.job_title;

SELECT * FROM SalaryByJobTitle
ORDER BY totalsalary DESC 
LIMIT 1;


CREATE VIEW EmployeeDependents AS
SELECT e.first_name, e.last_name, e.phone_number, COUNT(d.dependent_id) AS dependents
FROM employees e 
LEFT JOIN dependents d on d.employee_id = e.employee_id 
GROUP BY e.first_name, e.last_name, e.phone_number;

SELECT * FROM EmployeeDependents 
WHERE dependents = 0;


CREATE VIEW CountryLocation AS 
SELECT c.country_name, COUNT(l.location_id) as locations
FROM countries c 
LEFT JOIN locations l on l.country_id = c.country_id
GROUP BY c.country_name;

SELECT * FROM CountryLocation 
WHERE locations = 0;