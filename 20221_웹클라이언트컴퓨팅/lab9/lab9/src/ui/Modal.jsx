import React from 'react';
import PropTypes from 'prop-types';
import { withStyles, css } from './withStyles';

const Modal = ( props ) => {
    const { styles, children } = props;
    return (
      <div {...css(styles.overlay)}>
        <div {...css(styles.wrapper)}>
          <div {...css(styles.container)}>
            {children}
          </div>
        </div>
      </div>
    );
}

Modal.propTypes = {
  children: PropTypes.node,
};

export default withStyles(({ color, unit }) => ({
  overlay: {
    position: 'fixed',
    zIndex: 9999,
    top: 0,
    left: 0,
    width: '100%',
    height: '100%',
    backgroundColor: 'rgba(0, 0, 0, .5)',
  },
  wrapper: {
    verticalAlign: 'middle',
  },
  container: {
    margin: '40px auto 0px',
    padding: unit * 4,
    backgroundColor: color.white,
    width: 400,
  },
}))(Modal);
