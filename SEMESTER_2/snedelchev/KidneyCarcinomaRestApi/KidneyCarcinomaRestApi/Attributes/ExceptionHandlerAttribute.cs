namespace KidneyCarcinomaRestApi.Attributes
{
    using Microsoft.AspNetCore.Mvc;
    using Microsoft.AspNetCore.Mvc.Filters;

    using KidneyCarcinomaRestApi.Exceptions;
    using KidneyCarcinomaRestApi.Interfaces;
    using KidneyCarcinomaRestApi.Services;

    public class ExceptionHandlerAttribute : ExceptionFilterAttribute
    {
        private const string UnspecifiedErrorMessage = "Unspecified error occurred!";
        
        public override void OnException(ExceptionContext context)
        {
            IApiExceptionVisitor apiExceptionVisitor = new ApiExceptionVisitor();
            dynamic apiException = context.Exception;
            
            context.Result = ApiException.IsBaseClassOfException(apiException)
                ? apiExceptionVisitor.Visit(apiException)
                : new BadRequestObjectResult(UnspecifiedErrorMessage);

            context.Result = ErrorResponseBuilder.GetErrorResponse(context);
            
            base.OnException(context);
        }
    }
}