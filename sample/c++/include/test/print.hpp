#ifndef PRINT_HPP_
#define PRINT_HPP_
#include <iostream>

template <typename Colection>
void print(const Colection& col)
{
  for (const auto& c: col) 
    std::cout << c << std::endl;
}












#endif //PRINT_HPP_
