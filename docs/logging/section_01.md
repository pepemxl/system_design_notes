# Log

Logging is typically a key aspect of any production application; this is because it is important to provide appropriate information to allow future investigation following some event or issue in such applications. These investigations include:

- **Diagnosing failures**; that is why did an application fail/crash.
- **Identifying unusual or unexpected behaviour**; which might not cause the application to fail but which may leave it in an unexpected state or where data may be corrupted, etc.
- **Identifying performance or capacity issues**; in such situations the application is performing as expected by it is not meeting some non-functional requirements associated with the speed at which it is operating or its ability to scale as the amount of data or the number of users grows.
- **Dealing with attempted malicious behaviour** in which some outside agent is attempting to affect the behaviour of the system or to acquire information which they should not have access to, etc. This could happen for example, if you are creating a Python web application and a user tries to hack into your web server.
- **Regulatory or legal compliance**. In some cases records of program execution may be required for regulatory or legal reasons. This is particularly true of the financial sector where records must be kept for many years in case there is a need to investigate the organisations' or individuals' behaviour. 

The core elements of the logging framework (some of which are optional) are shown above and described below:

- **Log Message** The is the message to be logged from the application.
- **Logger** Provides the programmers entry point/interface to the logging system. The Logger class provides a variety of methods that can be used to log messages at different levels.
- **Handler** Handlers determine where to send a log message, default handlers include file handlers that send messages to a file and HTTP handlers that send messages to a web server.
- **Filter** This is an optional element in the logging pipeline. They can be used to further filter the information to be logged providing fine-grained control of which log messages are actually output (e.g. to a log file).•Formatter These are used to format the log message as required. This may involve adding timestamps, module and function/method information, etc. to the original log message.•Configuration Information The logger (and associated handlers, filters and formatters) can be configured either programmatically in Python or through configuration files. These configuration files can be written using key-value pairs or in a YAML file (which is a simple markup language). YAML stands for Yet Another Markup Language! It is worth noting that much of the logging framework is hidden from the developer who really only sees the logger; the remainder of the logging pipeline is either configured by default or via log configuration information typically in the form of a log configuration file. 36.2  The Logger The Logger provides the programmers interface to the logging pipeline. A Logger object is obtained from the getLogger() function defined in the logging module. The following code snippet illustrates acquiring the default logger and using it to log an error message. Note that the logging module must be imported: import logging logger = logging.getLogger() logger.error(’This should be used with something unexpected’)
36.3 Controlling the Amount of Information Logged399The output from this short application is logged to the console as this is the default configuration: This should be used with something unexpected 36.3  Controlling the Amount of Information Logged Log messages are actually associated with a log level. These log levels are intended to indicate the severity of the message being logged. There are six different log levels associated with the Python logging framework; these are:•NOTSET At this level no logging takes place and logging is effectively turned off.•DEBUG This level is intended to provide detailed information, typically of interest when a developer is diagnosing a bug or issues within an application.•INFO This level is expected to provide less detail than the DEBUG log level as it is expected to provide information that can be used to confirm that the application is working as expected.•WARNING This is used to provide information on an unexpected event or an indication of some likely problem that a developer or system administration might wish to investigate further.•ERROR This is used to provide information on some serious issue or problem that the application has not been able to deal with and that is likely to mean that the application cannot function correctly.•CRITICAL This is the highest level of issue and is reserved for critical situations such as ones in which the program can no longer continue executing. 




## Elastic Stack

ELK -- Elastic Logstash Kibana





