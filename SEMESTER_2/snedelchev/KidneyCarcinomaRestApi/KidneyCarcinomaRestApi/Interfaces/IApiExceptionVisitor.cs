namespace KidneyCarcinomaRestApi.Interfaces
{
    using Microsoft.AspNetCore.Mvc;

    using KidneyCarcinomaRestApi.Exceptions;

    public interface IApiExceptionVisitor
    {
        public IActionResult Visit(ApiBadRequestException exception);
        
        public IActionResult Visit(ApiNotFoundException exception);
    }
}