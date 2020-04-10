using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Nep;
using Newtonsoft.Json;



public class Example : MonoBehaviour // Change MonoBehaviour name for your class in unity
{
    // NEP objects as global
    Node node;
    Publisher pub;

    // Example of message to send
    class Msg
    {
        public int message { get; set; }
    }
    Msg msg2send;

    // Start is called before the first frame update
    void Start()
    {
        // Definition of objects
        node = new Node("unity_pub");
        pub = node.new_pub("test", "json");
        msg2send = new Msg();

    }

    // Update is called once per frame
    void Update()
    {
        msg2send.message = msg2send.message + 1;
        // Publish message
        pub.publish(msg2send);

    }

    // Called when program is finished
    void OnDestroy()
    {
        // IMPORTANT: Close objects to avoid freezing of Unity
        pub.close();
        node.close();
        Debug.Log("NEP objects closed");
    }

}