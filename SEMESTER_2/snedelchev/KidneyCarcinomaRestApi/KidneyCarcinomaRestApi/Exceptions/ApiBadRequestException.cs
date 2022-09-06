namespace KidneyCarcinomaRestApi.Exceptions
{
    using System;

    public class ApiBadRequestException : ApiException
    {
        private static readonly string DefaultMessage = "Incorrect value of the '{0}' parameter";

        public ApiBadRequestException(string parameter)
            : base(string.Format(DefaultMessage, parameter))
        {
            this.Parameter = parameter;
        }

        public ApiBadRequestException(string message, Exception inner)
            : base(message, inner)
        {
        }
        
        public string Parameter { get; }
    }
}