import java.util.Scanner;

/*
 * Name: GradeCalculator.java
 * Date: January,19th 2018
 * Version: v0.1
 * Author: Ryan Protheroe (SN: 20069587) (netID: 17RCP)
 */

public class GradeCalculator {

	// Initializing variables
	private static Scanner input;
	static int assignment1Weight = 0;
	static int assignment2Weight = 0;
	static int finalExamWeight = 0;
	static int classSize = 0;
	static Student[] classList = {}; // initializing length to 0
	static int[] studentNumbersUsed = {}; // initializing length to 0

	public static void main(String[] args) {
		System.out.println("Grade Calculator (Version 0.1). Author: Ryan Protheroe)");
		int choice = 0;
		while (choice != 9) { // Keeps program running until chosen to quit
			System.out.print("\n");
			choice = selection(); // Prints menu and gets user choice
			if (choice == 1) {
				if (classSize != 0) { // If a past simulation was ran, it sets all status' of students to false
					for (int i = 0; i < classList.length; i++) {
						classList[i].setStatus(false);
					}
				}
				assignment1Weight = 0; // resetting variables specific to new class
				assignment2Weight = 0;
				finalExamWeight = 0;
				classSize = 0;
				Student[] tempList = simulateCourseMarks(); // creating list of new class (running method)
				if (tempList != null) { // assures proper weights entered
					for (int i = 0; i < tempList.length; i++) { // combining list of new students with old students
						classList = arrayStudentPush(tempList[i], classList);
					}
				}
			} else if (choice == 2) {
				if (classSize != 0) { // assuring students exist
					System.out.println("Enter student number:");
					int studentNumber = input.nextInt(); // getting user input of student number
					viewOrUpdateMarks(studentNumber); // running method
				} else {
					System.out.println("<<< ERROR: Empty class list >>> \n Run option 1 first!");
				}
			} else if (choice == 3) {
				printClassReport(classList); // printing class report (running method)
			}
		}
		System.out.println("Thank you for using Grade Calculator (Version 0.1). Goodbye.");
		System.exit(0); // exiting program
	}

	public static boolean viewOrUpdateMarks(int studentNumber) {
		boolean exist = false; // used to assure student exists
		if (studentNumber >= 10000000 & studentNumber <= 99999999) { // assuring a valid student number
			for (int i = 0; i < classList.length; i++) { // loops through classList and assures a current student
				if (classList[i].getStudentNumber() == studentNumber && classList[i].getStatus() == true) {
					exist = true;
					Student student = classList[i];
					String choice = "";
					while (!choice.toUpperCase().equals("V") && !choice.toUpperCase().equals("U")) { // assures input
						System.out.println("View or Update? (V / U):");
						choice = input.next();
					}
					choice = choice.toUpperCase();
					if (choice.equals("V")) {
						reportHeader(); // prints header of report
						System.out.print(student.getStudentNumber()); // prints student number + marks
						System.out.print("		"); // spacing for report
						System.out.print(student.getMark("A1"));
						System.out.print("		");
						System.out.print(student.getMark("A2"));
						System.out.print("		");
						System.out.print(student.getMark("FE"));
						System.out.print("		");
						System.out.print(calculateFinalMark(student) + "\n"); // calculates final mark
					} else { // If user picks "U" (UPDATE)
						while (!choice.toUpperCase().equals("A1") && !choice.toUpperCase().equals("A2")
								&& !choice.toUpperCase().equals("FE")) { // assures a proper mark type
							System.out.println("Mark Type? (A1, A2 or FE):");
							choice = input.next();
						}
						System.out.println(choice.toUpperCase() + " is " + student.getMark(choice)); // prints mark
						int mark = -1;
						System.out.println("Updated Mark (0-100):");
						mark = input.nextInt();
						if (mark < 0 || mark > 100) { // assures proper mark value
							System.out.println(mark + " is an invalid mark");
							return false; // sends user back to menu
						} else {
							student.updateMark(choice, mark);
							return true; // sends user back to menu
						}
					}
				}
			}
			if (exist == false) {
				System.out.println(studentNumber + " is not in the current class or does not exist.");
			}
		} else {
			System.out.println(studentNumber + " is invalid.");
		}
		return false; // sends user back to menu
	}

	public static Student[] simulateCourseMarks() {
		input = new Scanner(System.in);
		while (classSize < 1) { // assures valid enrollment size
			System.out.println("Enter course enrollment size:");
			classSize = input.nextInt();
		}
		Student[] tempList = new Student[classSize]; // creates class list with proper size
		while (assignment1Weight == 0 || assignment1Weight < 20 || assignment1Weight > 30) { // assures proper weight
			System.out.println("Enter weight assignment 1 (20-30):");
			assignment1Weight = input.nextInt();
		}
		while (assignment2Weight == 0 || assignment2Weight < 20 || assignment2Weight > 30) {// assures proper weight
			System.out.println("Enter weight assignment 2 (20-30):");
			assignment2Weight = input.nextInt();
		}
		while (finalExamWeight == 0 || finalExamWeight < 40 || finalExamWeight > 60) {// assures proper weight
			System.out.println("Enter weight final exam (40-60):");
			finalExamWeight = input.nextInt();
		}
		if (assignment1Weight + assignment2Weight + finalExamWeight != 100) {// assures weights add to 100
			assignment1Weight = 0;// resets inputs from simulation
			assignment2Weight = 0;
			finalExamWeight = 0;
			classSize = 0;
			System.out.println("<<< ERROR: Weights do not add up to 100% >>> \n");
			return null; // exits method
		}
		for (int i = 0; i < classSize; i++) { // creates students
			int studentNumber = (int) (Math.random() * 90000000 + 10000000); // generates random student numbers
			for (int n = 0; n < studentNumbersUsed.length; n++) { // checks to see if student number has been used
				if (studentNumbersUsed[n] == studentNumber) {
					studentNumber = (int) (Math.random() * 90000000 + 10000000); // new number if number in use
					n = -1; // resets loop
				}
			}
			studentNumbersUsed = arrayIntPush(studentNumber, studentNumbersUsed); // adds number to array of used
																					// numbers
			Student student = generateStudentMarks(studentNumber); // generates student
			tempList[i] = student; // adds student to "classList"
		}
		return tempList; // returns array of generated students
	}

	// adds new integer to end of array
	public static int[] arrayIntPush(int item, int[] oldArray) {
		int len = oldArray.length;
		int[] newArray = new int[len + 1];
		System.arraycopy(oldArray, 0, newArray, 0, len);
		newArray[len] = item;
		return newArray;
	}

	// adds new Student to end of array
	public static Student[] arrayStudentPush(Student item, Student[] oldArray) {
		int len = oldArray.length;
		Student[] newArray = new Student[len + 1];
		System.arraycopy(oldArray, 0, newArray, 0, len);
		newArray[len] = item;
		return newArray;
	}

	public static int selection() {
		int choice = 0;
		input = new Scanner(System.in);
		while (choice != 1 || choice != 2 || choice != 3 || choice != 9) { // assures proper choice
			System.out.println("1 – Simulate Course Marks\r\n" + "2 – View/Update Student Marks\r\n"
					+ "3 – Run Mark Statistics\r\n" + "Select Option [1, 2 or 3] (9 to Quit):");
			choice = input.nextInt();
			if (choice == 1 || choice == 2 || choice == 3 || choice == 9) { // returns proper value
				return choice;
			} else {
				System.out.println("Invalid Selection\n");
			}
		}
		return choice;
	}

	public static Student generateStudentMarks(int studentNumber) {
		Student student = new Student(studentNumber); // creates student object with identifier
		int a1 = (int) (Math.random() * 100); // assigns random marks from 0 - 100 for each mark type
		student.updateMark("A1", a1);
		int a2 = (int) (Math.random() * 100);
		student.updateMark("A2", a2);
		int fe = (int) (Math.random() * 100);
		student.updateMark("FE", fe);
		return student; // returns student
	}

	// printing headers of report
	public static void reportHeader() {
		System.out.print("Student Number		");
		System.out.print("A1(" + assignment1Weight + "%)		");
		System.out.print("A2(" + assignment2Weight + "%)		");
		System.out.print("FE(" + finalExamWeight + "%)		");
		System.out.print("Final Mark");
		System.out.print("\n");
		System.out.print("______________		");
		System.out.print("_______	 	");
		System.out.print("_______	 	");
		System.out.print("_______	 	");
		System.out.print("___________");
		System.out.print("\n");
	}

	public static void printClassReport(Student[] students) {
		reportHeader(); // printing header
		if (classList.length != 0) {
			int a1Total = 0; // calculating totals for each mark type to calculate averages
			int a2Total = 0;
			int feTotal = 0;
			int fmTotal = 0;
			int highestFinal = 0; // pre-setting highest and lowest finals
			int lowestFinal = 100;
			for (int i = 0; i < classList.length; i++) {
				if (classList[i].getStatus() == true) { // assuring active student
					System.out.print(classList[i].getStudentNumber()); // printing student statistics
					System.out.print("		"); // proper spacing
					System.out.print(classList[i].getMark("A1"));
					a1Total += classList[i].getMark("A1");
					System.out.print("		");
					System.out.print(classList[i].getMark("A2"));
					a2Total += classList[i].getMark("A2");
					System.out.print("		");
					System.out.print(classList[i].getMark("FE"));
					feTotal += classList[i].getMark("FE");
					System.out.print("		");
					System.out.print(calculateFinalMark(classList[i]) + "\n");
					fmTotal += calculateFinalMark(classList[i]);
					if (calculateFinalMark(classList[i]) > highestFinal) { // checking final mark for highest
						highestFinal = calculateFinalMark(classList[i]);
					}
					if (calculateFinalMark(classList[i]) < lowestFinal) { // checking final mark for lowest
						lowestFinal = calculateFinalMark(classList[i]);
					}
				}
			}
			System.out.print("______________		"); // printing bottom of report
			System.out.print("_______	 	");
			System.out.print("_______	 	");
			System.out.print("_______	 	");
			System.out.print("___________\n");
			System.out.print("AVERAGES		");
			System.out.print(a1Total / classSize + "		"); // calculating average for mark type
			System.out.print(a2Total / classSize + "		");
			System.out.print(feTotal / classSize + "		");
			System.out.print(fmTotal / classSize + "\n");
			System.out.println("Highest final mark is " + highestFinal);
			System.out.println("Lowest final mark is " + lowestFinal + "\n");

		} else {
			System.out.println("<<Empty List/ No Students>> \n");

		}
		System.out.println("Press Enter to Continue");
		input.nextLine(); // waiting for user to hit enter
		input.nextLine();
	}

	public static int calculateFinalMark(Student student) {
		int a1 = (int) (student.getMark("A1") * (.01 * assignment1Weight)); // using the weights to calculate final
		int a2 = (int) (student.getMark("A2") * (.01 * assignment2Weight));
		int fe = (int) (student.getMark("FE") * (.01 * finalExamWeight));
		return a1 + a2 + fe; // returning final mark
	}
}
