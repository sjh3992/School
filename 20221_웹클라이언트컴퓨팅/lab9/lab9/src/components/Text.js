import React from 'react';
import styled from 'styled-components';

const TextBlock = styled.div`
  display: flex;
  padding: 1rem;
  width: 768px;
  margin: 0 auto;
  @media screen and (max-width: 768px) {
    width: 100%;
    overflow-x: auto;
  }
`;

const TextBox = ( ) => {
      return (
        <TextBlock>
            뉴스 개수:
            <textarea
                rows={6}
                style={{textAlign:"left", width:"768px"}}
            />
        </TextBlock>
        );
};

export default TextBox;