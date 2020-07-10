import React, {Component} from 'react';
import PropTypes from 'prop-types';

/**
 * It takes a for-loop to delete multiples traces, and
 * then append the new ones.
 */

export default class EditableGraph extends Component {    
    render() {
       const {id, aim, data, style, setProps} = this.props;
       if (document.getElementById(aim) && data.disable == null) {
         var gd = document.getElementById(aim);
         var i;
         var arr = [];                
    
         for (i = 0; i <= gd.data.length-1; i++) {          
          if (gd.data[i] != null){           
           arr.push(i);                     
           } 

         }
         Plotly.deleteTraces(gd, arr); 
         Plotly.addTraces(gd, data);  
    
       }
       return (
            <div id = {id} style = {style}></div>
        );
    }
}

EditableGraph.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id : PropTypes.string.isRequired,
    /**
     * The ID used in the dcc.Graph to modify.
     */
    aim : PropTypes.string.isRequired,
    /**
     * A list of dic with the data to update
     */
    data : PropTypes.array,
    /**
     * A object with the data style
     */
    style: PropTypes.object
};

EditableGraph.defaultProps = {
    data : {disable:'yes'}
}; 
