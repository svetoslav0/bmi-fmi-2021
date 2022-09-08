namespace KidneyCarcinomaRestApi.Exceptions
{
    using System;
    using KidneyCarcinomaRestApi.Interfaces;
    using Microsoft.AspNetCore.Mvc;

    public abstract class ApiException : Exception
    {
        public ApiException(string message)
            : base(message)
        {
        }
        
        public ApiException(string message, Exception innerEx)
            : base(message, innerEx)
        {
        }
        
        public static bool IsBaseClassOfException(dynamic apiException)
        {
            return apiException.GetType().IsSubclassOf(typeof(ApiException));
        }
        
        public abstract IActionResult Accept(IApiExceptionVisitor visitor);
    }
}