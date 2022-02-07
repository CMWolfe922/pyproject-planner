# PROJECT DESIGN AND SPECIFICATIONS

> PyPlanner is a gui application that helps with the process of laying out a projects design specifications. It is meant to make things simpler when it comes to planning the design of a new app or project. By having everything layout in a visible manner, it helps guide you throughout the whole process of:

	- Identifying a problem 
	- Assessing the problem
	- Coming up with questions to ask to solve the problem
		- Then answering those questions
	- Information about the data 
	- Information about the users
	- Document the specifications
---

## PROJECT SECTIONS:

> _SECTION (A)_ __Project Summary__: Gets the project name, authors, version number, and short description (500 characters)

> _SECTION (B)_ __Requirements__: Get the input and output requirements, calculations needed, features the program must have, and soft requirements(things youd like to add if possible or in another version)

> _SECTION (C)_ __Not Required__: Multiline input box that takes in what isn't required. 

> _SECTION (D)_ __Limitations__: List any of the projects limitations due to software, hardware, skill, costs, and performance.

> _SECTION (E)_ __Data Dictionary__: This is a table that is used to layout all the projects data types. It will have the columns (FIELD, DATATYPE, UNITS, RANGE, DESCRIPTION) _I may add a column for grouping so that the users can more easily group the data together._

> _SECTION (F)_ __Widget Types__: This is a table for labeling what kind of widget will be used for each type of data.

> _SECTION (G)_ __Widget Grouping__: This will be a table that allows you to pick which widgets go in which group. This will be helpful in determining the GUI layout. 

---

#### DOCUMENTING SPECIFICATION REQUIREMENTS

> __Description__ --> This is one or two sentences that describe the primary purpose, function, and goals of the application. Think of it as the program's mission statement.

> __Functionality Required__ --> This section is a list of specific things the program needs to be able to do to be minimally functional. It can include both hardrequirements, such as detailed output and input formats, and soft requirements—goals that are not quantifiably attainable, but that the program should strive toward (for example, "reduce user errors as much as possible").

> __Functionality NOT Required__ -->  This section is a list of things the program does not need to do; it exists to clarify the scope of the software and make sure nobody expects unreasonable things from the application.

> __Limitations__ --> This is a list of constraints under which the program must operate, both technological and human.

> __Data Dictionary__ --> This is a detailed list of the data fields the application will deal with and their parameters. These can get quite lengthy but are a critical referenceas the application expands and the data gets utilized in other contexts.

---
### EXAMPLE OF HOW THE TXT FILE WILL LOOK ONCE SUBMITTED:

```
====================================
ABQ Data Entry Program specification
====================================

Description
-----------

The program is being created to minimize data entry errors for
laboratory measurements.


Functionality Required
----------------------

The program must:

    * allow all relevant, valid data to be entered, as per the field
    chart.
    * append entered data to a CSV file
        - The CSV file must have a filename
          of abq_data_record_CURRENTDATE.csv, where
          CURRENTDATE is the date of the checks in
          ISO format (year-month-day)
        - The CSV file must have all the fields as per the chart
    * enforce correct datatypes per field

The program should try, whenever possible, to:
    
    * enforce reasonable limits on data entered
    * Auto-fill data
    * Suggest likely correct values
    * Provide a smooth and efficient workflow

Funcionality NOT Required
-------------------------

The program does not need to:

    * Allow editing of data. This can be done in LibreOffice if
    necessary.
    * Allow deletion of data.

Limitations
-----------

The program must:

    * Be effecient
    * Be accessible to color blind users.
    * Run on Debian Linux.
    * Run acceptably on low-end computers

Data Dictionary
---------------

+------------+----------+------+--------------+---------------------+
|Field       | Datatype | Units| Range        |Descripton
|
+============+==========+======+==============+=====================+
|Date        |Date      |      |              |Date of record
|
+------------+----------+------+--------------+---------------------+
|Time        |Time      |      |8, 12, 16, 20 |Time period
|
+------------+----------+------+--------------+---------------------+
|Lab         |String    |      | A - E        |Lab ID
|
+------------+----------+------+--------------+---------------------+
|Technician  |String    |      |              |Technician name
|
+------------+----------+------+--------------+---------------------+
|Plot        |Int       |      | 1 - 20       |Plot ID
|
+------------+----------+------+--------------+---------------------+
|Seed sample |String    |      |              |Seed sample ID
|
+------------+----------+------+--------------+---------------------+
|Fault       |Bool      |      |              |Fault on sensor
|
+------------+----------+------+--------------+---------------------+
|Light       |Decimal   |klx   | 0 - 100      |Light at plot
|
+------------+----------+------+--------------+---------------------+
|Humidity    |Decimal   |g/m³  | 0.5 - 52.0   |Abs humidity at plot
|
+------------+----------+------+--------------+---------------------+
|Temperature |Decimal   |°C    | 4 - 40       |Temperature at plot
|
+------------+----------+------+--------------+---------------------+
|Blossoms    |Int       |      | 0 - 1000     |# blossoms in plot
|
+------------+----------+------+--------------+---------------------+
|Fruit       |Int       |      | 0 - 1000     |# fruits in plot
|
+------------+----------+------+--------------+---------------------+
|Plants      |Int       |      | 0 - 20       |# plants in plot
|
+------------+----------+------+--------------+---------------------+
|Max height  |Decimal   |cm    | 0 - 1000     |Ht of tallest plant
|
+------------+----------+------+--------------+---------------------+
|Min height  |Decimal   |cm    | 0 - 1000     |Ht of shortest plant
|
+------------+----------+------+--------------+---------------------+
|Medianheight|Decimal   |cm    | 0 - 1000     |Median ht of plants
|
+------------+----------+------+--------------+---------------------+
|Notes       |String    |      |              |Miscellaneous notes
|
+------------+----------+------+--------------+---------------------+
```
---

