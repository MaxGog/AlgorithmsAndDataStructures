using System.Collections.ObjectModel;
using System.Windows.Input;

using CommunityToolkit.Mvvm.ComponentModel;

using ListBooks.Models;
using ListBooks.Data;
using ListBooks.Views;

namespace ListBooks.ViewModels;

public class MainViewModel : ObservableObject
{
    private readonly BookData data = new();
    private ObservableCollection<CardModel> books;
    public ObservableCollection<CardModel> Books
    {
        get => books ??= new ObservableCollection<CardModel>();
        set => SetProperty(ref books, value);
    }

    public ICommand openFileCommand { get; private set; }
    public ICommand addBookCommand { get; private set; }
    public ICommand sortNameCommand { get; private set; }
    public ICommand sortAuthorCommand { get; private set; }
    public ICommand sortPlaceCommand { get; private set; }
    public ICommand sortDateCommand { get; private set; }


    public MainViewModel() 
    { 
        openFileCommand = new Command(() => LoadBooksAsync());
        sortNameCommand = new Command(() => SortedByName());
        sortAuthorCommand = new Command(() => SortedByAuthor());
        sortPlaceCommand = new Command(() => SortedByPlace());
        sortDateCommand = new Command(() => SortedByDate());
    }

    private async Task LoadBooksAsync()
    {
        try
        {
            await data.AddContentAsync();
            var booksList = data.GetBooks();
            Books.Clear();
            foreach (var book in booksList)
            {
                Books.Add(book);
            }
            await Application.Current.MainPage.DisplayAlert("Файлы загружены", $"Загружено {Books.Count} книг", "OK");
        }
        catch (Exception ex) { await Application.Current.MainPage.DisplayAlert("Ошибка", $"Произошла ошибка при загрузке файлов: {ex.Message}", "OK"); }
    }

    private void SortedByName()
    {
        var sortedBooks = Books.OrderBy(x => x.NameBook).ToList();
        Books = new ObservableCollection<CardModel>(sortedBooks);
    }
    private void SortedByAuthor()
    {
        var sortedBooks = Books.OrderBy(x => x.Author).ToList();
        Books = new ObservableCollection<CardModel>(sortedBooks);
    }
    private void SortedByPlace()
    {
        var sortedBooks = Books.OrderBy(x => x.PublicationPlace).ToList();
        Books = new ObservableCollection<CardModel>(sortedBooks);
    }
    private void SortedByDate()
    {
        var sortedBooks = Books.OrderBy(x => x.PublicationDate).ToList();
        Books = new ObservableCollection<CardModel>(sortedBooks);
    }

}