# question-paper-generatorQuestion Paper Generator
Problem Definition:
Design and implement a Question Paper Generator
The application must store a number of questions in a Question Store. A question can have the
following attributes {question_id, difficulty, marks}
The Question paper Generator should be capable of generating Question Paper based on the
number of marks and distribution of marks based on Difficulty.
Do note that the questions with same difficulty level can have different marks.
Example​ :
(100 marks, {20% Easy, 50% Medium, 30% Hard })
This means that we are required to generate a question paper of 100 marks which 20% (ie 20
marks) worth of questions having Difficulty=Easy, 50% having Difficulty=Medium and 30%
having Difficulty=Hard
Requirements:
Should support this using In-Memory DS constructs, use of DB is not allowed.
Expectations:
1.
2.
3.
4.
5.
6.
Create the sample data yourself. You can put it into a file.
The code should be demoable.
Code should be modular.
Code should be extensible.
Code should handle edge cases properly and fail gracefully.
Code should be readable.
Guidelines:
1. Please do not access internet for anything EXCEPT syntax.
2. You are free to use language of your choice
3. All work should be your own.Sample​ :
1. Input​ (I’ve added the total number of questions in the first line, followed by the question
details, followed by the ​ total marks ​ needed for the question paper along with the difficulty
level and marks. Feel free to use a different format (reading from file in json format etc).
Do note that the total marks here is 20 ) ​
10
Q1, easy, 1
Q2, easy, 2
Q3, medium, 2
Q4, hard, 9
Q5, easy, 3
Q6, hard, 7
Q7, medium, 3
Q8, easy, 3
Q9, medium, 5
Q10, hard, 5
20, easy 25, medium, 50, hard 25
Output​ (The split is given in percentage. The question paper should have questions with
difficulty level = easy for 5 marks, medium for 10 marks, hard for 5 marks)
Q2
Q5
Q10
Q3
Q9
Q7
