//Password generator


Console.WriteLine("Welcome to my password generator! ");
//options: len of password, include symbols, numbers, capital letters(first/random/all)
Console.WriteLine("");
Console.WriteLine("Select options: ");
Console.WriteLine("1 for password length");
Console.WriteLine("2 for including symbols");
Console.WriteLine("3 for including numbers");
Console.WriteLine("4 for capital letters");
Console.WriteLine("5 for generating the password");

Boolean Generated = false;
Boolean Symbols = false;
Boolean Numbers = false;
Boolean Capital = false;
String password = "";
int length = 8;

while (Generated != true)
{
    Console.WriteLine("");
    Console.WriteLine("Input: ");
    String Answer = Console.ReadLine();

    switch (Answer)
    {
        case "1":
            Console.WriteLine("Type in how many characters you need");
            length = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Saved");
            break;
        case "2":
            Symbols = true;
            Console.WriteLine("Symbols are enabled");
            break;
        case "3":
            Numbers = true;
            Console.WriteLine("Numbers are enabled");
            break;
        case "4":
            Capital = true;
            Console.WriteLine("Saved");
            break;
        case "5":
            Generated = true;
            break;
        default:
            Console.WriteLine("Try again");
            break;
    }
}
// ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789
if (Symbols == false && Numbers == false && Capital == false)
{
    var chars = "abcdefghijklmnopqrstuvwxyz";
    var stringChars = new char[length];
    var random = new Random();

    for (int i = 0; i < stringChars.Length; i++)
    {
        stringChars[i] = chars[random.Next(chars.Length)];
    }

    var finalString = new String(stringChars);
    Console.WriteLine("");
    Console.WriteLine("Your password is: " + finalString);
}


if (Symbols == true && Numbers == false && Capital == false)
{
    var chars = "abcdefghijklmnopqrstuvwxyz!@#$%^&*()_+|=[]?><;:'";
    var stringChars = new char[length];
    var random = new Random();

    for (int i = 0; i < stringChars.Length; i++)
    {
        stringChars[i] = chars[random.Next(chars.Length)];
    }

    var finalString = new String(stringChars);
    Console.WriteLine("");
    Console.WriteLine("Your password is: " + finalString);
}

if (Symbols == true && Numbers == true && Capital == false)
{
    var chars = "abcdefghijklmnopqrstuvwxyz!@#$%^&*()_+|=[]?><;:'1234567890";
    var stringChars = new char[length];
    var random = new Random();

    for (int i = 0; i < stringChars.Length; i++)
    {
        stringChars[i] = chars[random.Next(chars.Length)];
    }

    var finalString = new String(stringChars);
    Console.WriteLine("");
    Console.WriteLine("Your password is: " + finalString);
}

if (Symbols == false && Numbers == true && Capital == false)
{
    var chars = "abcdefghijklmnopqrstuvwxyz1234567890";
    var stringChars = new char[length];
    var random = new Random();

    for (int i = 0; i < stringChars.Length; i++)
    {
        stringChars[i] = chars[random.Next(chars.Length)];
    }

    var finalString = new String(stringChars);
    Console.WriteLine("");
    Console.WriteLine("Your password is: " + finalString);
}
//

if (Symbols == false && Numbers == true && Capital == true)
{
    var chars = "ABCDEFGHIJKLMNOPQRSTUVWXYabcdefghijklmnopqrstuvwxyz1234567890";
    var stringChars = new char[length];
    var random = new Random();

    for (int i = 0; i < stringChars.Length; i++)
    {
        stringChars[i] = chars[random.Next(chars.Length)];
    }

    var finalString = new String(stringChars);
    Console.WriteLine("");
    Console.WriteLine("Your password is: " + finalString);
}

if (Symbols == true && Numbers == false && Capital == true)
{
    var chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()_+|=[]?><;:'";
    var stringChars = new char[length];
    var random = new Random();

    for (int i = 0; i < stringChars.Length; i++)
    {
        stringChars[i] = chars[random.Next(chars.Length)];
    }

    var finalString = new String(stringChars);
    Console.WriteLine("");
    Console.WriteLine("Your password is: " + finalString);
}

//
if (Symbols == false && Numbers == false && Capital == true)
{
    var chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
    var stringChars = new char[length];
    var random = new Random();

    for (int i = 0; i < stringChars.Length; i++)
    {
        stringChars[i] = chars[random.Next(chars.Length)];
    }

    var finalString = new String(stringChars);
    Console.WriteLine("");
    Console.WriteLine("Your password is: " + finalString);
}





if (Symbols == true && Numbers == true && Capital == false)
{
    var chars = "abcdefghijklmnopqrstuvwxyz!@#$%^&*()_+|=[]?><;:'1234567890";
    var stringChars = new char[length];
    var random = new Random();

    for (int i = 0; i < stringChars.Length; i++)
    {
        stringChars[i] = chars[random.Next(chars.Length)];
    }

    var finalString = new String(stringChars);
    Console.WriteLine("");
    Console.WriteLine("Your password is: " + finalString);
}

if (Symbols == true && Numbers == true && Capital == true)
{
    var chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()_+|=[]?><;:'1234567890";
    var stringChars = new char[length];
    var random = new Random();

    for (int i = 0; i < stringChars.Length; i++)
    {
        stringChars[i] = chars[random.Next(chars.Length)];
    }

    var finalString = new String(stringChars);
    Console.WriteLine("");
    Console.WriteLine("Your password is: " + finalString);
}