using Nep;
using System.Threading;
using Newtonsoft.Json;

namespace Example // Change this namespace by your project namespace
{
    class Program
    {
        // Message to listen, must be exactly the same keys
        class Msg
        {
            // JSON key = message, value is a string
            public string message { get; set; }
        }

        static void Main(string[] args)
        {
            // Definition of objects
            Nep.Node node = new Nep.Node("csharp_sender");
            Nep.Subscriber sub = node.new_sub("test", "json");

            // Message as strings to convert to Msg
            string msg = "";
            bool isMsg = false;

            // print message and finish
            while (!isMsg)
            {
                // Non blocking listen
                isMsg = sub.listenNB(ref msg);

                // if isMsg == true, then msg has information, otherwise, there is no message
                if (isMsg)
                {
                    // Convert JSON string to Msg 
                    Msg message = JsonConvert.DeserializeObject<Msg>(msg);
                    Console.WriteLine(message.message);
                }
            }

            // See message 2 seconds
            Thread.Sleep(2000);
            // Close sockets
            sub.close();
            node.close();
        }
    }
}

