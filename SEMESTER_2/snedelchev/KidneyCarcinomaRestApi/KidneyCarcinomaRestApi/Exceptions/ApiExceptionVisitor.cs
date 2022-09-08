namespace KidneyCarcinomaRestApi.Exceptions
{
    using Microsoft.AspNetCore.Mvc;

    using KidneyCarcinomaRestApi.Interfaces;

    public class ApiExceptionVisitor : IApiExceptionVisitor
    {
        public IActionResult Visit(ApiBadRequestException exception)
        {
            return new BadRequestObjectResult(exception.Message);
        }

        public IActionResult Visit(ApiNotFoundException exception)
        {
            return new NotFoundObjectResult(exception.Message);
        }
    }
}