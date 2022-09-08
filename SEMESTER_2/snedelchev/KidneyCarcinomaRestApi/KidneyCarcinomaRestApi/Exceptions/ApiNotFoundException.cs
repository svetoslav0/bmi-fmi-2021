namespace KidneyCarcinomaRestApi.Exceptions
{
    using System;
    using KidneyCarcinomaRestApi.Interfaces;
    using Microsoft.AspNetCore.Mvc;

    public class ApiNotFoundException : ApiException
    {
        private static readonly string DefaultMessage = "'{0}' with id '{1}' can not be found!";

        public ApiNotFoundException(string message, string parameter)
            : base(message)
        {
            this.Parameter = parameter;
        }

        public ApiNotFoundException(string item, string value, string parameter)
            : base(string.Format(DefaultMessage, item, value))
        {
            this.Item = item;
            this.Parameter = parameter;
            this.ParamValue = value;
        }

        public ApiNotFoundException(string message, Exception inner)
            : base(message, inner)
        {
        }
        
        public string Item { get; }

        public string Parameter { get; }
        
        public string ParamValue { get; }
        
        public override IActionResult Accept(IApiExceptionVisitor visitor)
        {
            return visitor.Visit(this);
        }
    }
}