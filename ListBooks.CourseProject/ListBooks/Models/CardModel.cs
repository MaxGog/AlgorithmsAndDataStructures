namespace ListBooks.Models;

public class CardModel
{
    public int Id { get; set; }
    public string NameBook { get; set; }
    public string Author { get; set; }
    public DateTime PublicationDate { get; set; }
    public string PublicationPlace { get; set; }
    public string Description { get; set; }
    
}