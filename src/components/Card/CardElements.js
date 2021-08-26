import styled from "styled-components";


export const CardWrapper = styled.div`
  overflow: hidden;
  padding: 0 0 32px;
  margin: 60px auto 0;
  width: 300px;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.05), 0 0px 40px rgba(0, 0, 0, 0.08);
  border-radius: 50px 50px 50px 50px;
  border: 5px solid red;
  border-color: #000;
`;

export const CardImage = styled.img`
  padding-top: 2px;
  padding-bottom: 2px;
  width: 100%;
  max-hight: 100px;
`;

export const CardHeader = styled.header`
  padding-top: 10px;
  padding-bottom: 10px;
`;

export const CardHeading = styled.h1`
  font-size: 24px;
  font-weight: bold;
  text-align: center;
`;

export const CardBody = styled.div`
  padding-right: 32px;
  padding-left: 32px;
`;

export const CardDescription = styled.div`
padding-bottom: 10px;

font-size: 15px;
color: gray;
text-align: left;
`;




export const CardFieldset = styled.fieldset`
  position: relative;
  padding: 0;
  margin: 0;
  border: 0;

  & + & {
    margin-top: 24px;
  }

  &:nth-last-of-type(2) {
    margin-top: 32px;
  }

  &:last-of-type {
    text-align: center;
  }
`;




export const CardButton = styled.button`
  display: block;
  width: 100%;
  padding: 12px 0;
  font-family: inherit;
  font-size: 14px;
  font-weight: 700;
  color: #fff;
  background-color: #256ce1;
  border: 0;
  border-radius: 35px;
  box-shadow: 0 10px 10px rgba(0, 0, 0, 0.08);
  cursor: pointer;
  transition: all 0.25s cubic-bezier(0.02, 0.01, 0.47, 1);

  &:hover {
    box-shadow: 0 15px 15px rgba(0, 0, 0, 0.16);
    transform: translate(0, -5px);
  }
`;
