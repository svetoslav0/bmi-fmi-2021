namespace KidneyCarcinomaRestApi.Attributes
{
    using System;
    using System.Linq;
    using System.Reflection;
    using Microsoft.AspNetCore.Mvc;
    using Microsoft.AspNetCore.Mvc.Filters;
    
    using KidneyCarcinomaRestApi.Exceptions;
    using KidneyCarcinomaRestApi.Models;
    using KidneyCarcinomaRestApi.Models.Parameters;

    public class PaginatedAttribute : ActionFilterAttribute
    {
        protected readonly string Limit = "Limit";

        protected readonly string Offset = "Offset";

        protected readonly string Parameters = "parameters";

        protected readonly string LimitErrorMessage = "The limit parameter should be from {0} to {1}";

        protected readonly string OffsetErrorMessage = "The offset parameter should be more than or equal to {0}";
        
        private readonly int defaultLimit;

        private readonly int defaultOffset;
        
        public PaginatedAttribute(int defaultLimit, int defaultOffset)
        {
            this.defaultLimit = defaultLimit;
            this.defaultOffset = defaultOffset;
        }
        
        protected virtual int LimitMin { get; set; } = 1;

        protected virtual int LimitMax { get; set; } = 100;
        
        protected virtual int OffsetMin { get; set; } = 0;

        public override void OnActionExecuting(ActionExecutingContext filterContext)
        {
            this.SetDefaultLimits();
            this.CheckLimitValue(filterContext);
            this.CheckOffsetOrCursorValue(filterContext);

            if (!filterContext.ModelState.IsValid)
            {
                var errorMessage = filterContext.ModelState.Values.ToArray().Where(e => e.Errors.Any()).FirstOrDefault()?.Errors.FirstOrDefault()?.ErrorMessage;
                filterContext.Result = new BadRequestObjectResult(errorMessage);
                throw new ApiBadRequestException(errorMessage, null);
            }
        }
        
        protected virtual void SetDefaultLimits()
        {
            this.LimitMax = this.defaultLimit;
            this.LimitMin = this.defaultOffset;
        }
        
        protected virtual void CheckLimitValue(ActionExecutingContext filterContext)
        {
            this.TrySetDefaultValueFor(filterContext, this.Limit, this.defaultLimit);

            int limit = ((AbstractParameters)filterContext.ActionArguments[this.Parameters]).Limit;

            if (limit < this.LimitMin || limit > this.LimitMax)
            {
                filterContext.ModelState.AddModelError(this.Limit, string.Format(this.LimitErrorMessage, this.LimitMin, this.LimitMax));
            }
        }
        
        protected virtual void CheckOffsetOrCursorValue(ActionExecutingContext filterContext)
        {
            this.TrySetDefaultValueFor(filterContext, this.Offset, this.defaultOffset);

            int offset = ((AbstractParameters)filterContext.ActionArguments[this.Parameters]).Offset.Value;

            if (offset < this.OffsetMin)
            {
                filterContext.ModelState.AddModelError(this.Offset, string.Format(this.OffsetErrorMessage, this.OffsetMin));
            }
        }
        
        private void TrySetDefaultValueFor(ActionExecutingContext filterContext, string param, int value)
        {
            var paramsObject = (AbstractParameters)filterContext.ActionArguments[this.Parameters];
            var propType = paramsObject.GetType();
            var property = propType.GetProperty(param);

            if (this.HasPropertyDefaultValue(property, paramsObject))
            {
                property.SetValue(
                    paramsObject, 
                    Convert.ChangeType(value, Nullable.GetUnderlyingType(property.PropertyType) ?? property.PropertyType), 
                    null);
            }
        }
        
        private bool HasPropertyDefaultValue(PropertyInfo property, AbstractParameters paramsObject)
        {
            var propertyValue = property.GetValue(paramsObject);
            var type = property.PropertyType;

            if (type == typeof(int))
            {
                return (int)propertyValue == 0;
            }

            return propertyValue == null;
        }
    }
}