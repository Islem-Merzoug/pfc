import styled from 'styled-components';

export const Pupup = styled.nav`
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    hight: 100hv;
    background-color: #fff

    display: flex;
    justify-content: center;
    align-items: center;
`;

export const PupupInner = styled.nav`
    position: relative;
    padding: 32px;
    width: 100%;
    width: 100hv;
    max-width: 640px;
    background-color: #fff

    position: absolute;
    top: 16px;
    right: 16px;
`;

export const CloseBtn  = styled.nav`
    position: absolute;
    top: 16px;
    right: 16px;
`;