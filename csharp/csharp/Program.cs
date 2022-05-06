/* 
 * Fizz buzz because it's well known, rules per https://en.wikipedia.org/wiki/Fizz_buzz
 * any number divisible by three is replaced by the word fizz and any number divisible by 
 * five by the word buzz. Numbers divisible by 15 become fizz buzz
 */
Console.WriteLine("fizz buzz please enter a number");
string userAnswer = Console.ReadLine();

// Parse string to int - hopefully TryParse has some exception handling
try
{
    int.TryParse()
}
// Catch null exception
catch (NullReferenceException)
{
    Console.WriteLine("Please enter a number");
}
// fizz buzz logic goes here
if (userAnswer % 5)
{

}