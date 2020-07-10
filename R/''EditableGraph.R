# AUTO GENERATED FILE - DO NOT EDIT

''EditableGraph <- function(id=NULL, aim=NULL, data=NULL, style=NULL) {
    
    props <- list(id=id, aim=aim, data=data, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'EditableGraph',
        namespace = 'dash_update_data_components',
        propNames = c('id', 'aim', 'data', 'style'),
        package = 'dashUpdateDataComponents'
        )

    structure(component, class = c('dash_component', 'list'))
}
