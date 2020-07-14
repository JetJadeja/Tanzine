# TanzineLang
Tanzine is a new, basic programming language written and interpreted in Python. It is able to utilize Python's standard libraries as well a libraries on the [Python Package Index](https://pypi.org/). Using Tanzine, you are able to acheive relatives imports, however package installation is not yet completed. 

## Please join our Discord server for help or ways to get involved: https://discord.gg/4aWwGQ4

### Warning
Tanzine is an extremely new language, so there is no installation process. We are currently working on an installer to add the **tanzine** command to your path. 
The Tanzine Tutorial listed below also does not cover **everything**. The Tanzine core team is working on Docs!

## Basics
Tanzine's syntax is simple to understand. Each statement comes after a definitive, which will tell tanzine what type of statement you are making. A definitive looks something like this: `@DEFINITIVE@`.

Statements in Tanzine are similar to those in other languages. For example, math is the exact same (besides definitives)! Let's add two numbers! Type: `@MATH@ 5 + 2`. Since we do not display anything, nothing happens. So, let's assign a variable to the output of *5 + 2* and then display it in the console. 

To assign variables, we can use the VAR definitive (`@VAR@`) followed by the variable name. So we could do `@VAR@ num` (however that would display an error). Next we can write an equal symbol and then the statement that we are setting the variable to. 

So we can type: `@VAR@ num = @MATH@ 5 + 2`. And there you go! We have defined a variable!

Now to print this variable we need to use the `print` function. To run functions, we must use the RUN definitive (`@RUN@`) followed by the function and parameters. The syntax for a function is `(function,arg1,arg2,arg3)`. **Note the lack of spaces between the arguments**! To use variables as arguments, we need to use the `@` symbol followed by the variable name. So, our variable `num` would be `@num` in our function. We can type `@RUN@ (/print,@num)` to print *num* out. This will output `7`! Full code: 
```
@VAR@ num = @MATH@ 5 + 2
@RUN@ (/print,@num)
```
Full output:
```
7
```

**More basics are yet to come!**

## Quick Start Guide
First, you must start an app using Tanzine start app. `tanzine startapp AppName`. If you do not specify an app name, Tanzine will create one called *TanzineApp*. We can just use the default app name. Type `tanzine startapp`.

Next, open your IDE of Choice and open our *TanzineApp* directory. There should be a file called **main.tzn**. You  can open this file and start making some changes!

**More will be added to Quick Start Guide**

### More Information
The Code behind Tanzine was made in just 3 hours (we've added more features, though). **This means that the Tanzine code isn't pretty. The Development team is going to work on fixing this**.

## Please join our Discord server for help or ways to get involved: https://discord.gg/4aWwGQ4
The server has a Discord bot (called Tater) allowing you to run Tanzine code directly in Discord, and see the output as a response message from the bot. 
- Whenever an error is not covered by Tanzine, the bot **will create an issue in the repository**!
- Mention the bot by typing `@Tater` for instructions!

# Dev Team
The core dev team currently consists of:

[JetDeveloping](https://github.com/JetDeveloping)

[TransmissionsDev](https://github.com/TransmissionsDev)
