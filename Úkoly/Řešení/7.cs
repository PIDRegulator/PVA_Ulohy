using setup_game;
using System;
using System.Collections.Generic;
using System.Dynamic;
using System.Security.Cryptography.X509Certificates;
using static Game;

namespace setup_game
{
    public class Hrac
    {
        public string Name { get; set; }
        public int Score { get; set; }

        public Hrac(string name)
        {
            Name = name;
            Score = 0;
        }
    }

    public class program
    {
        public static int pocet_hracu = 0;

        public static List<Hrac> Player_list()
        {
            List<Hrac> list = new List<Hrac>();

            while (true)
            {
                Console.Write("Zadejte počet hráčů (2 - 5): ");
                if (int.TryParse(Console.ReadLine(), out pocet_hracu) && pocet_hracu >= 2 && pocet_hracu <= 5)
                {
                    break;
                }
                Console.WriteLine("Neplatný počet hráčů");
            }

            for (int i = 0; i < pocet_hracu; i++)
            {
                Console.Write($"Zadejte jméno hráče {i + 1}: ");
                string name = Console.ReadLine();
                list.Add(new Hrac(name));
            }

            return list;
        }
    }

    
}


public class Game
{
    public class Dice
    {
        public static (int, int) Dice_numbers()
        {
            Random Dice_1 = new Random();
            int dice1 = Dice_1.Next(1, 6);
            int dice2 = Dice_1.Next(1, 6);
            Console.WriteLine($"Generated number: {dice1 +" and "+ dice2}");
            return (dice1, dice2);
            

        }
    }
    public static void Main()
    {
        // Starting game
        Console.WriteLine("START");

        // Get the list of players
        List<Hrac> hraci = setup_game.program.Player_list();

        

        // Example loop using pocet_hracu and displaying player information
        for (int i = 0; i < setup_game.program.pocet_hracu; i++)
        {
            var hrac = hraci[i];
            Console.WriteLine($"Hráč {i + 1}: Jméno: {hrac.Name}, Skóre: {hrac.Score}");
        }

        while (true)
        {
            //Console.Clear();
            for (int i = 0; i <  setup_game.program.pocet_hracu; i++)
            {
                Console.ReadKey();
                var hrac = hraci[i];
                Console.WriteLine("\n______________________________________________");
                Console.WriteLine(hrac.Name);
                (int dice1,int dice2) = Dice.Dice_numbers();
                
                if (dice1 == 1 && dice2 == 1)
                {
                    Console.WriteLine("Both 1 so loosing all points");
                    hrac.Score = 0;
                    
                }
                else if (dice1 == 1 || dice2 == 1)
                {
                    Console.WriteLine("One is 1 so end of turn");
                    

                }
                else
                {
                    Console.WriteLine($"Adding {dice1 + dice2} to your score");
                    hrac.Score += dice1 + dice2;
                }



                if (hrac.Score >= 100)
                {
                    Console.WriteLine("END OF GAME!");
                    Console.WriteLine($"{hrac} WON THE GAME!!");
                    Console.ReadKey();
                    
                    return;
                    
                }
                else
                {
                    Console.WriteLine("Players Score is: " + hrac.Score);
                }

                
                
            }
            Console.ReadKey();
            Console.WriteLine("______________________________________________");
            for (int i = 0; i < setup_game.program.pocet_hracu; i++)
            {
                var hrac = hraci[i];

                Console.WriteLine($"Hráč {i + 1}: Jméno: {hrac.Name}, Skóre: {hrac.Score}");
            }
           
        }

    }
}
