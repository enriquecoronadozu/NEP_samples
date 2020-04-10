
using Nep;
using Newtonsoft.Json;


namespace Example // Use you project instead
{
    class Program
    {
        class Msg
        {
            public string message { get; set; }
        }

        static void Main(string[] args)
        {
            // Definition of objects
            Nep.Node node = new Nep.Node("csharp_sender");
            Nep.Publisher pub = node.new_pub("test", "json");
            // Message to send
            Msg msg = new Msg();
            // Fill message
            msg.message = "hello";
            // Publish message
            pub.publish(msg);
            // Close sockets
            pub.close();
            node.close();
        }
    }
}
