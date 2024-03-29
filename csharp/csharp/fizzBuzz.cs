﻿/* 
 * Fizz buzz because it's well known, rules per https://en.wikipedia.org/wiki/Fizz_buzz
 * any number divisible by three is replaced by the word fizz and any number divisible by 
 * five by the word buzz. Numbers divisible by 15 become fizz buzz
 */
bool program = true;
while (program == true)
{
    Console.WriteLine("please enter a number or type quit");

    int answer;
   
    var userAnswer = int.TryParse(Console.ReadLine(), out answer);
    
    if (userAnswer == false)
    {
        program = false;
        break;
    }
    if (answer % 15 == 0 )
    {
        Console.WriteLine("fizz buzz");
    }
    else if (answer % 5 == 0)
    {
        Console.WriteLine("buzz");
    }
    else if (answer % 3 == 0)
    {
        Console.WriteLine("fizz");
    }
    else
    {
        Console.WriteLine(answer);
    }
}