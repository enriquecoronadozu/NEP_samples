using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Nep;
using Newtonsoft.Json;

public class Example : MonoBehaviour // Change MonoBehaviour name for your class in unity
{
    // NEP objects as global
    Node node;
    Subscriber sub;

    // Example of message to send
    class Msg
    {
        public string message { get; set; }
    }

    // Message as strings to convert to Msg
    string msg;


    // Start is called before the first frame update
    void Start()
    {
        // Definition of objects
        node = new Node("unity_sub");
        sub = node.new_sub("test", "json");
    }

    // Update is called once per frame
    void Update()
    {
        // Non blocking listen
        bool isMsg = sub.listenNB(ref msg);
        // if isMsg == true, then msg has information, otherwise, there is no message
        if (isMsg)
        {
            // Convert JSON string to Msg 
            Msg message = JsonConvert.DeserializeObject<Msg>(msg);
            Debug.Log(message.message);
        }

    }

    // Called when program is finished
    void OnDestroy()
    {
        // IMPORTANT: Close objects to avoid freezing of Unity
        sub.close();
        node.close();
        Debug.Log("NEP objects closed");
    }

}