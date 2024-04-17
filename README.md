**Attendance Tracker README**

**Description:**
This Python script provides a graphical user interface (GUI) for tracking attendance and assigning points to individuals based on various attendance types. It utilizes the Tkinter library for GUI development and SQLite for data storage.

**Dependencies:**
- Python 3.x
- Tkinter
- SQLite3

**Setup:**
1. Ensure Python is installed on your system.
2. Install Tkinter library (if not already installed) using:
   ```
   pip install tk
   ```
3. No additional installation is required for SQLite3 as it comes bundled with Python.

**Usage:**
1. Run the script using a Python interpreter.
2. The GUI window titled "Attendance Tracker" will appear.
3. Enter the name of the individual in the provided entry field.
4. Select the attendance type from the drop-down menu.
5. Click the "Submit" button to record the attendance and assign points.
6. A notification will appear at the bottom indicating that the record has been updated.

**Point System:**
- **Forced Early out - before two hours:** 1.0 point
- **Forced earlyout After two hours:** 0.5 points
- **Call out:** 1.0 point
- **Call out consecutive:** 0.5 points
- **Late:** 0.5 points
- **No call no show:** 6.0 points

**Example Queries:**
- To count the total points for a specific name:
  ```sql
  SELECT SUM(points) FROM attendance WHERE name = 'John';
  ```

**Updating and Deleting Points:**
- Updating points is not directly implemented in this script. However, you can manually modify the points for a specific entry in the SQLite database using SQL commands.
- To delete a record:
  ```sql
  DELETE FROM attendance WHERE id = <id>;
  ```
  Replace `<id>` with the ID of the record you want to delete.

**Note:**
- Make sure to handle database backups and security measures as needed for your application's requirements.
- This script provides basic functionality and can be extended further based on specific project needs.