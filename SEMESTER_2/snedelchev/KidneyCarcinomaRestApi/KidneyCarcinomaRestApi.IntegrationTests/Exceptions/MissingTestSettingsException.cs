namespace KidneyCarcinomaRestApi.IntegrationTests.Exceptions
{
    using System;

    public class MissingTestSettingsException : Exception
    {
        public MissingTestSettingsException()
        {
        }

        public MissingTestSettingsException(string message)
            : base(message)
        {
        }

        public MissingTestSettingsException(string message, Exception inner)
            : base(message, inner)
        {
        }
    }
}
