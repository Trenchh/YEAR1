/*
 * Name: Student.java
 * Date: January,19th 2018
 * Version: v0.1
 * Author: Ryan Protheroe (SN: 20069587) (netID: 17RCP)
 */

public class Student {

	int studentNumber;
	boolean status;
	int assignment1Mark;
	int assignment2Mark;
	int finalExamMark;

	Student(int n) {
		// Assuring a valid student number
		if (n >= 10000000 & n <= 99999999) {
			studentNumber = n;
			status = true;
		} else {
			System.out.println("Invalid Student Number");
			status = false;
		}
	}

	// Used to set students of older simulations status' to false
	public void setStatus(boolean newStatus) {
		status = newStatus;
	}

	public boolean updateMark(String markType, int mark) {
		if (mark >= 0 && mark <= 100) { // Assures mark is valid
			switch (markType.toUpperCase()) { // Assigns mark to appropriate mark type
			case "A1":
				assignment1Mark = mark;
				System.out.println("Assignment 1 Mark Updated"); // User feedback to assure proper mark was updated
				return true; // Exits method
			case "A2":
				assignment2Mark = mark;
				System.out.println("Assignment 2 Mark Updated");
				return true;
			case "FE":
				finalExamMark = mark;
				System.out.println("Final Exam Mark Updated");
				return true;
			default:
				System.out.println("Invalid Mark Type");
				return false;
			}
		} else {
			System.out.println("Invalid Mark"); // User feedback assuring mark is not in range
			return false;
		}
	}

	public int getMark(String markType) {
		switch (markType.toUpperCase()) { // Grabs mark based on mark type entered
		case "A1":
			return assignment1Mark;
		case "A2":
			return assignment2Mark;
		case "FE":
			return finalExamMark;
		default:
			System.out.println("Invalid Mark Type"); // base case, meaning if no "match" is found, -1 is returned
			return -1;
		}
	}

	// returns student number
	public int getStudentNumber() {
		return studentNumber;
	}

	// Same as constructor method, updates and validates student number
	public void setStudentNumber(int n) {
		if (n >= 10000000 & n <= 99999999) {
			studentNumber = n;
			status = true;
		} else {
			System.out.println("Invalid Student Number");
			status = false;
		}
	}

	// returns validity of student object
	public boolean getStatus() {
		return status;
	}
}
